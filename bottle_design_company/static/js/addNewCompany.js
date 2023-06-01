window.addEventListener('DOMContentLoaded', () => {
    const newCompanyButton = document.querySelector('#newCompanyButton')
    const newCompanyForm = document.querySelector('#newCompanyForm')
    const formButton = document.querySelector('#formButton')
    newCompanyButton.addEventListener('click', () => {
        newCompanyButton.style.display = "none"
        newCompanyForm.style.display = "flex"
    })
    formButton.addEventListener('click', () => {
        newCompanyButton.style.display = "block"
        newCompanyForm.style.display = "none"
    })
})