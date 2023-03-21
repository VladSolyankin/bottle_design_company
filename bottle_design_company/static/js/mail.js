let sendButton = document.querySelector(".info__button-submit")
let message = document.querySelector('textarea')

sendButton.addEventListener('click', (e) => {
	document.querySelector('.main__content').action =
		`mailto:ourmail@example.com?body=${message.textContent}`
})
