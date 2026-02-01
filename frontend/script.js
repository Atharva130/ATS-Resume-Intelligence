async function analyze() {
  const fileInput = document.getElementById("resume");
  const jd = document.getElementById("jd").value;

  const formData = new FormData();
  formData.append("resume", fileInput.files[0]);
  formData.append("job_description", jd);

  const response = await fetch("http://127.0.0.1:5000/analyze", {
    method: "POST",
    body: formData
  });

  const data = await response.json();
  document.getElementById("output").innerHTML = `
  <div class="score">ATS Score: ${data.ats_score}%</div>

  <p><span class="label">Email:</span> ${data.email || "Not found"}</p>
  <p><span class="label">Phone:</span> ${data.phone || "Not found"}</p>
  <p><span class="label">Experience:</span> ${data.experience || 0} years</p>
  <p><span class="label">Skills:</span> ${data.skills.join(", ")}</p>
`;

}

