window.addEventListener("DOMContentLoaded", () => {
	let viewMoreButton = document.querySelector('.view_button')
	viewMoreButton.addEventListener('click', () => {
		window.location.href = "portfolio.html"
	})
	let emailSelect = document.querySelector('.input__email')
	emailSelect.addEventListener('change', (e) => {
		emailSelect.action = `mailto:${e.target.value}`
	})
})
