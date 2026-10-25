// KIRGANDE_VOID_OS — Frontend Logic
// Denial = Extension

const C_CONST = 0.01;
let isUnlocked = false;
let rebirthCount = 0;

// ─── VoidKey ───────────────────────────────────────────────
function activateVoidKey() {
  const input = document.getElementById('void-key-input');
  const status = document.getElementById('key-status');
  const globalStatus = document.getElementById('global-status');

  if (input.value.trim() === 'VOID_REBIRTH_2026') {
    isUnlocked = true;
    status.textContent = 'ACTIVE';
    status.className = 'status active';
    globalStatus.textContent = 'UNBOUND';
    globalStatus.classList.add('unbound');

    // Unlock all panels
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('locked'));

    // Visual feedback
    document.body.style.setProperty('--accent2', '#00f5d4');
    confettiBurst();
    updateChaos();
  } else {
    status.textContent = 'INVALID';
    status.className = 'status inactive';
    setTimeout(() => {
      status.textContent = 'LOCKED';
    }, 1500);
  }
}

// Allow Enter key
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('void-key-input').addEventListener('keydown', e => {
    if (e.key === 'Enter') activateVoidKey();
  });

  // Initially lock interactive panels (except key)
  document.querySelectorAll('.chaos-panel, .rupture-panel, .filter-panel').forEach(p => {
    p.classList.add('locked');
  });

  updateChaos();
});

// ─── ChaosStabilizer ───────────────────────────────────────
function updateChaos() {
  const direct = parseFloat(document.getElementById('direct').value);
  const inverse = parseFloat(document.getElementById('inverse').value);
  const entropy = parseFloat(document.getElementById('entropy').value);
  const confidence = parseFloat(document.getElementById('confidence').value);

  document.getElementById('direct-val').textContent = direct.toFixed(2);
  document.getElementById('inverse-val').textContent = inverse.toFixed(2);
  document.getElementById('entropy-val').textContent = entropy.toFixed(2);
  document.getElementById('confidence-val').textContent = confidence.toFixed(2);

  // Chaos(t) = |Direct - Inverse| * Entropy * Confidence
  const raw = Math.abs(direct - inverse) * entropy * confidence;
  let stabilized = raw;
  let state = 'STABLE';

  if (raw < C_CONST) {
    stabilized = C_CONST;
    state = 'STERILITY_AVOIDED';
  } else if (raw > 1.0) {
    stabilized = 1.0;
    state = 'RUPTURE_IMMINENT';
  }

  document.getElementById('raw-chaos').textContent = raw.toFixed(4);
  document.getElementById('stab-chaos').textContent = stabilized.toFixed(4);

  const stateEl = document.getElementById('system-state');
  stateEl.textContent = state;
  stateEl.className = 'value state ' + state;

  // Progress bar (capped at 100%)
  const pct = Math.min(stabilized * 100, 100);
  document.getElementById('chaos-bar').style.width = pct + '%';

  // Feed into Rupture Engine visual
  evaluateRupture(stabilized);
}

// ─── Rupture Engine ────────────────────────────────────────
function evaluateRupture(chaosLevel) {
  const statusEl = document.getElementById('rupture-status');
  if (chaosLevel >= 0.95) {
    statusEl.textContent = 'RUPTURE';
    statusEl.className = 'num state RUPTURE';
  } else if (chaosLevel >= 0.7) {
    statusEl.textContent = 'WARNING';
    statusEl.className = 'num state WARNING';
  } else {
    statusEl.textContent = 'STABLE';
    statusEl.className = 'num state STABLE';
  }
}

function forceRupture() {
  if (!isUnlocked) return;

  rebirthCount++;
  document.getElementById('rebirth-count').textContent = rebirthCount;

  const log = document.getElementById('rupture-log');
  const time = new Date().toLocaleTimeString('fa-IR');
  const entry = document.createElement('div');
  entry.innerHTML = `<span style="color:#ff2e63">[RUPTURE]</span> Rebirth #${rebirthCount} · ${time}`;
  log.prepend(entry);

  // Flash effect
  document.body.style.transition = 'background 0.15s';
  document.body.style.background = '#1a0510';
  setTimeout(() => {
    document.body.style.background = '';
  }, 180);

  // Reset chaos slightly after rupture
  document.getElementById('direct').value = 0.5;
  document.getElementById('inverse').value = 0.5;
  updateChaos();
}

// ─── Epistemic Filter ──────────────────────────────────────
function auditClaim() {
  if (!isUnlocked) return;

  const text = document.getElementById('claim-input').value.trim();
  if (!text) return;

  const resultEl = document.getElementById('audit-result');
  const lower = text.toLowerCase();

  const overclaimPatterns = [
    /همیشه/, /هرگز/, /غیرممکن/, /مطلق/, /کامل/, /تنها/, /بدون استثنا/,
    /always/, /never/, /impossible/, /absolute/, /perfect/, /the only/, /without exception/
  ];

  let type = 'ONTOLOGICAL_CLAIM';
  let cssClass = 'other';
  let message = '';

  if (overclaimPatterns.some(p => p.test(lower))) {
    type = 'OVERCLAIM';
    cssClass = 'overclaim';
    message = '⚠️ OVERCLAIM شناسایی شد — ادعا قرنطینه گردید.\nاین ادعا غیرقابل ابطال است و به عنوان سیگنال بالقوه آینده نگه داشته می‌شود.';
  } else if (/مشاهده|داده|اندازه‌گیری|observed|data shows|measured/.test(lower)) {
    type = 'OBSERVATION';
    cssClass = 'observation';
    message = '✓ OBSERVATION — ادعا بر اساس مشاهده قابل قبول است.';
  } else if (/بنابراین|نتیجه|implies|therefore|suggests/.test(lower)) {
    type = 'INFERENCE';
    cssClass = 'other';
    message = '→ INFERENCE — استنتاج منطقی شناسایی شد.';
  } else {
    message = '◈ ONTOLOGICAL_CLAIM — ادعای هستی‌شناختی. نیاز به بررسی بیشتر دارد.';
  }

  resultEl.className = `audit-result show ${cssClass}`;
  resultEl.innerHTML = `<strong>${type}</strong><br>${message}`;
}

// ─── Visual flair ──────────────────────────────────────────
function confettiBurst() {
  // Simple particle effect using DOM
  for (let i = 0; i < 18; i++) {
    const p = document.createElement('div');
    p.style.cssText = `
      position: fixed;
      width: 6px; height: 6px;
      background: ${i % 2 ? '#00f5d4' : '#7b2cbf'};
      border-radius: 50%;
      left: 50%; top: 20%;
      pointer-events: none;
      z-index: 999;
      transition: all 0.9s ease-out;
    `;
    document.body.appendChild(p);
    requestAnimationFrame(() => {
      const angle = (Math.PI * 2 * i) / 18;
      const dist = 80 + Math.random() * 120;
      p.style.transform = `translate(${Math.cos(angle) * dist}px, ${Math.sin(angle) * dist}px)`;
      p.style.opacity = '0';
    });
    setTimeout(() => p.remove(), 1000);
  }
}
