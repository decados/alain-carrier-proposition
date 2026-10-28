// Seul le geste explicite sur le lien ouvre le logiciel de courriel.
if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) if (entry.isIntersecting) {
      entry.target.classList.add('in-view');
      observer.unobserve(entry.target);
    }
  }, {threshold: 0.08});
  document.querySelectorAll('main h2, main h3, main p, main figure, main blockquote, main img:not(.hero-photo), .faq-list details, .composer').forEach(element => observer.observe(element));
}

const compose = document.querySelector('#compose-email');
compose.addEventListener('click', () => {
  const selected = [...document.querySelectorAll('.choices input:checked')].map(input => input.value);
  const subject = 'Premier contact — célébration hommage';
  const body = selected.length
    ? `Bonjour Alain,\n\nJ’aimerais vous parler d’une célébration hommage. J’aimerais notamment évoquer : ${selected.join(', ')}.\n\nMerci,\n`
    : 'Bonjour Alain,\n\nJ’aimerais vous parler d’une célébration hommage.\n\nMerci,\n';
  compose.href = `mailto:alaincarrier.cla@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
});
