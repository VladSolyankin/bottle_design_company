const companyImage = document.getElementById("companyImage")
const imagePicker = document.getElementById("imagePicker")
imagePicker.addEventListener('change', (e) => {
	companyImage.classList.remove("hide")
	let files = e.target.files
	let fr = new FileReader();
	fr.addEventListener('load', () => {
		companyImage.src = window.URL.createObjectURL(files[0])
		console.log(companyImage.src)
	})
	fr.readAsDataURL(files[0])
})