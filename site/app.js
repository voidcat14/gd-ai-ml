const messagesEl = document.getElementById('messages');
const form = document.getElementById('chatForm');
const input = document.getElementById('input');
const send = document.getElementById('send');
const settings = document.getElementById('settings');
const backendUrl = document.getElementById('backendUrl');
const provider = document.getElementById('provider');
const ownerModel = document.getElementById('ownerModel');

backendUrl.value = localStorage.getItem('aichater_backend') || '';
provider.value = localStorage.getItem('aichater_provider') || 'OpenRouter';
ownerModel.value = localStorage.getItem('aichater_model') || '';

document.getElementById('settingsBtn').onclick = () => settings.showModal();
document.getElementById('settingsForm').addEventListener('submit', () => {
  localStorage.setItem('aichater_backend', backendUrl.value.trim());
  localStorage.setItem('aichater_provider', provider.value);
  localStorage.setItem('aichater_model', ownerModel.value.trim());
});

document.getElementById('clearBtn').onclick = clearChat;
document.getElementById('newChat').onclick = clearChat;
document.querySelectorAll('[data-prompt]').forEach(button => {
  button.onclick = () => { input.value = button.dataset.prompt; input.focus(); };
});

input.addEventListener('input', () => {
  input.style.height = 'auto';
  input.style.height = Math.min(input.scrollHeight, 180) + 'px';
});
input.addEventListener('keydown', event => {
  if (event.key === 'Enter' && !event.shiftKey) {
    event.preventDefault();
    form.requestSubmit();
  }
});

function addMessage(role, text) {
  const welcome = messagesEl.querySelector('.welcome');
  if (welcome) welcome.remove();
  const row = document.createElement('div');
  row.className = `message ${role}`;
  const avatar = document.createElement('div');
  avatar.className = 'avatar';
  avatar.textContent = role === 'user' ? 'You' : '✦';
  const content = document.createElement('div');
  content.className = 'content';
  content.textContent = text;
  row.append(avatar, content);
  messagesEl.appendChild(row);
  messagesEl.scrollTop = messagesEl.scrollHeight;
  return content;
}

function clearChat() {
  messagesEl.innerHTML = `<div class="welcome"><div class="welcome-icon">✦</div><h1>What can I help with?</h1><p>AIChater is a ChatGPT-style interface designed to work with the model provider chosen by the server owner.</p><div class="cards"><button data-prompt="Explain how AI model providers work.">How do model providers work?</button><button data-prompt="Give me three ideas for a small AI project.">AI project ideas</button><button data-prompt="Explain OpenRouter in simple terms.">Explain OpenRouter</button></div></div>`;
  messagesEl.querySelectorAll('[data-prompt]').forEach(button => button.onclick = () => { input.value = button.dataset.prompt; input.focus(); });
}

async function sendToBackend(text, content) {
  const base = backendUrl.value.trim().replace(/\/$/, '');
  if (!base) return false;
  const response = await fetch(`${base}/api/chat`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({message: text, model: ownerModel.value.trim() || undefined})
  });
  if (!response.ok) throw new Error(`Backend returned ${response.status}`);
  const data = await response.json();
  content.textContent = data.message ?? data.response ?? data.content ?? JSON.stringify(data);
  return true;
}

form.addEventListener('submit', async event => {
  event.preventDefault();
  const text = input.value.trim();
  if (!text || send.disabled) return;
  addMessage('user', text);
  input.value = '';
  input.style.height = 'auto';
  send.disabled = true;
  const content = addMessage('assistant', 'Thinking…');
  try {
    const connected = await sendToBackend(text, content);
    if (!connected) {
      await new Promise(resolve => setTimeout(resolve, 450));
      content.textContent = `This is the AIChater demo. Your message was received:\n\n“${text}”\n\nConnect an AIChater backend in Settings to use a real model. The backend owner controls the provider, model, and API key.`;
    }
  } catch (error) {
    content.textContent = `I couldn't reach the configured AIChater backend. Check the Backend URL in Settings.\n\n${error.message}`;
  } finally {
    send.disabled = false;
    input.focus();
  }
});
