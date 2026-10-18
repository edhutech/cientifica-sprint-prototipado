(() => {
  'use strict';
  const slides = [...document.querySelectorAll('.slide')];
  let current = 0;
  let state = 0;
  let lastPointerAdvance = -Infinity;
  const live = document.getElementById('live-status');
  const controls = document.getElementById('controls');
  const counter = document.getElementById('counter');
  const maximum = () => Number(slides[current].dataset.maxState || 0);

  function update() {
    slides.forEach((slide, i) => {
      const active = i === current;
      slide.hidden = !active;
      slide.inert = !active;
      slide.setAttribute('aria-hidden', String(!active));
      slide.classList.toggle('active', active);
      if (active) {
        slide.dataset.state = String(state);
        slide.querySelectorAll('[data-states]').forEach(el => {
          const visible = el.dataset.states.split(',').map(Number).includes(state);
          el.hidden = !visible;
          el.setAttribute('aria-hidden', String(!visible));
        });
        slide.querySelectorAll('[data-from]').forEach(el => {
          const visible = state >= Number(el.dataset.from);
          el.hidden = !visible;
          el.setAttribute('aria-hidden', String(!visible));
        });
      }
    });
    const label = `${current + 1} / ${slides.length}`;
    counter.textContent = label;
    document.getElementById('previous').disabled = current === 0 && state === 0;
    document.getElementById('next').disabled = current === slides.length - 1 && state === maximum();
    controls.classList.toggle('on-cover', current === 0);
    controls.classList.toggle('on-blue', !!slides[current].querySelector('.section-blue'));
    controls.classList.toggle('on-orange', !!slides[current].querySelector('.activity-orange'));
    controls.dataset.slide = String(current + 1);
    const answer = [...slides[current].querySelectorAll('.answer:not([hidden])')].map(el => el.textContent.trim()).join('. ');
    live.textContent = `Diapositiva ${label}. ${slides[current].dataset.title}${answer ? '. ' + answer : ''}`;
    document.body.dataset.slide = String(current + 1);
    document.body.dataset.state = String(state);
    // Keep focus out of a section that just became hidden.
    if (document.activeElement.closest('.slide[hidden]')) document.getElementById('next').focus();
  }
  function go(index) {
    if (index < 0 || index >= slides.length) return;
    current = index;
    state = 0;
    update();
  }
  function next() {
    if (state < maximum()) { state++; update(); }
    else if (current < slides.length - 1) go(current + 1);
  }
  function previous() {
    if (state > 0) { state--; update(); }
    else if (current > 0) go(current - 1);
  }
  function reset() { state = 0; update(); }
  async function fullscreen() {
    try {
      if (document.fullscreenElement) await document.exitFullscreen();
      else await document.documentElement.requestFullscreen();
    } catch {
      live.textContent = 'Pantalla completa no disponible. Puede usar F11 en Chromium.';
    }
  }
  document.addEventListener('fullscreenchange', () => {
    const full = Boolean(document.fullscreenElement);
    document.getElementById('fullscreen').setAttribute('aria-pressed', String(full));
    document.getElementById('fullscreen').setAttribute('aria-label', full ? 'Salir de pantalla completa' : 'Pantalla completa');
  });
  const interactive = target => target.closest('a,button,input,textarea,select,[contenteditable="true"]');
  document.addEventListener('keydown', event => {
    if (event.repeat || event.ctrlKey || event.altKey || event.metaKey || event.target.closest('input,textarea,select,[contenteditable="true"]')) return;
    if (event.target.closest('a,button') && (event.key === ' ' || event.key === 'Enter')) return;
    const actions = {
      ArrowRight: next, ArrowDown: next, ' ': next, PageDown: next,
      ArrowLeft: previous, ArrowUp: previous, PageUp: previous,
      Home: () => go(0), End: () => go(slides.length - 1),
      r: reset, R: reset, f: fullscreen, F: fullscreen,
    };
    if (actions[event.key]) { event.preventDefault(); actions[event.key](); }
  });
  document.getElementById('previous').addEventListener('click', previous);
  document.getElementById('next').addEventListener('click', next);
  document.getElementById('fullscreen').addEventListener('click', fullscreen);
  document.addEventListener('click', event => {
    if (interactive(event.target) || !event.target.closest('.slide.active') || event.detail > 1 || getSelection().toString()) return;
    const now = performance.now();
    if (now - lastPointerAdvance < 250) return;
    lastPointerAdvance = now;
    next();
  });
  let touch = null;
  document.addEventListener('touchstart', event => {
    if (!interactive(event.target) && event.touches.length === 1) touch = { x: event.touches[0].clientX, y: event.touches[0].clientY };
  }, {passive:true});
  document.addEventListener('touchend', event => {
    if (!touch) return;
    const dx = event.changedTouches[0].clientX - touch.x;
    const dy = event.changedTouches[0].clientY - touch.y;
    touch = null;
    if (Math.abs(dx) > 60 && Math.abs(dx) > Math.abs(dy)) {
      event.preventDefault(); lastPointerAdvance = performance.now();
      dx < 0 ? next() : previous();
    }
  }, {passive:false});
  document.documentElement.classList.add('js');
  controls.hidden = false;
  update();
})();
