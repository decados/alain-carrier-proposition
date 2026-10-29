const compose = document.querySelector('#compose-email');
const messages = {
  hommage: ['Premier contact - célébration hommage', 'Bonjour Alain,\n\nJ’aimerais discuter de la préparation d’un hommage.\n\nMerci,\n'],
  question: ['Question sur les célébrations', 'Bonjour Alain,\n\nJ’aimerais vous poser une question au sujet des célébrations.\n\nMerci,\n']
};
function updateEmail() {
  const choice = document.querySelector('input[name="sujet"]:checked').value;
  const [subject, body] = messages[choice];
  compose.href = `mailto:alaincarrier.cla@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
}
document.querySelectorAll('input[name="sujet"]').forEach(input => input.addEventListener('change', updateEmail));
updateEmail();

if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const entrance = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('entered');
      entrance.unobserve(entry.target);
    });
  }, {threshold: 0.08});
  document.querySelectorAll('.hero-copy > *, .hero-photo, main h2, .intro > p, .intro-detail, .approach-steps > div, .about-voice, .context p, .contact-action').forEach(el => entrance.observe(el));
}
