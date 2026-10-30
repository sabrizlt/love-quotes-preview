document.documentElement.classList.add("js");

addEventListener("DOMContentLoaded", () => {
  const header = document.querySelector(".site-header");
  const onScroll = () => header.classList.toggle("scrolled", scrollY > 8);
  onScroll();
  addEventListener("scroll", onScroll, { passive: true });

  const seen = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add("in");
      seen.unobserve(entry.target);
    });
  }, { threshold: 0.08 });
  document.querySelectorAll(".reveal").forEach((node) => seen.observe(node));

  // Anteprima per il cliente: il modulo non invia niente.
  const form = document.querySelector("form");
  if (form) {
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      form.querySelector(".form-note").textContent = "Preview only: this form does not send messages yet.";
    });
  }
});
