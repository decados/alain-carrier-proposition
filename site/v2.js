const compose = document.querySelector("#compose-email");
const subjects = {
  hommage: {
    subject: "Premier contact - célébration hommage",
    body: "Bonjour Alain,\n\nJ’aimerais discuter de la préparation d’un hommage.\n\nMerci,\n",
  },
  question: {
    subject: "Question sur les célébrations",
    body: "Bonjour Alain,\n\nJ’aimerais vous poser une question au sujet des célébrations.\n\nMerci,\n",
  },
};

function updateEmail() {
  const choice = document.querySelector('input[name="sujet"]:checked').value;
  const { subject, body } = subjects[choice];
  compose.href = `mailto:alaincarrier.cla@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
}

document
  .querySelectorAll('input[name="sujet"]')
  .forEach((input) => input.addEventListener("change", updateEmail));
updateEmail();

if (
  "IntersectionObserver" in window &&
  !matchMedia("(prefers-reduced-motion: reduce)").matches
) {
  const stage = document.querySelector(".portrait-stage");
  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting)
          stage.classList.toggle(
            "is-close",
            entry.target.id === "accompagnement",
          );
      }
    },
    { rootMargin: "-35% 0px -35% 0px" },
  );
  document
    .querySelectorAll(
      "#alain, #ceremonies, #accompagnement, .parole, .reseau, #contact",
    )
    .forEach((section) => observer.observe(section));

  const entrances = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        entry.target.classList.add("entered");
        entrances.unobserve(entry.target);
      }
    },
    { threshold: 0.05 },
  );
  document
    .querySelectorAll(
      ".reading h1, .reading h2, .reading h3, .reading p, .reading blockquote, .reading img, .reading .button",
    )
    .forEach((element) => entrances.observe(element));
}
