import "django-gesha";

async function handleEnquiry(e: Event) {
  const form = document.getElementById("enquiry-form") as HTMLFormElement;
  const formFields = form.querySelector(".form-fields");
  const formData = new FormData(form);
  const url = window.django.reverse("enquiry");
  const response = await fetch(url, {
    method: "POST",
    mode: "same-origin",
    body: formData
  });
  const jsonData = await response.json();
  formFields.innerHTML = jsonData.form.as_p;
}

async function setupEnquiryForm() {
  const btn = document.querySelector("#enquiry-form [type=button]");
  btn.addEventListener("click", handleEnquiry);
}

setupEnquiryForm();
