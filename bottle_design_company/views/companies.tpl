<!DOCTYPE html>
<html lang="en">
<head>
	<title></title>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="../static/css/companies.css">
</head>
<body>
	<header class="index__header">
		<a href="index.html">
			<img src="../static/images/logo.png" alt="Design Company logo" class="header__logo">
		</a>

		<div class="header__menu">
			<ul class="header__menu-list">
				<li><a href="/home">HOME</a></li>
				<li><a href="/about">ABOUT US</a></li>
				<li><a href="/portfolio">PORTFOLIO</a></li>
				<li><a href="/contacts">CONTACTS</a></li>
				<li><a href="/articles">ARTICLES</a></li>
				<li><a href="/companies">COMPANIES</a></li>
			</ul>
		</div>
	</header>

	<main class="companies__container">
		<button class="form__button-submit" id="newCompanyButton">Add new company</button>
		<form class="addNewCompany__form" enctype="multipart/form-data" method="post" id="newCompanyForm">
			<p>Add new company:</p>
			<label>
				<input type="text" placeholder="Enter company name" name="TITLE" class="form__input" required>
			</label>
			<label>
				<textarea placeholder="Enter company description" name="DESCRIPTION" class="form__input" required></textarea>
			</label>
			<label>
				<input type="tel" placeholder="Phone number 8-xxx-xxx-xx-xx" name="PHONE" class="form__input" pattern="8-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}" required>
			</label>
			<input type="file" id="imagePicker" class="form__imagePicker form__input" name="IMAGE">
			<img src="" alt="some text" class="hide form__image-company" id="companyImage">
			<button type="submit" class="form__button-submit" id="formButton">Add new company</button>
		</form>
		<p class="error">{{error}}</p>
		<div class="companies__container-images">
			%with open('./companies.txt') as f:
			%	lines = f.readlines()
			%for i in lines:
			%	currentCompany = i.split(":")
				<div class="container__card-company">
					<img src="{{currentCompany[0]}}" class="container__img">
					<p class="title__text">{{currentCompany[1]}}</p>
					<p>{{currentCompany[2]}}</p>
					<p class="phone__text">{{currentCompany[3]}}<p>
				</div> 
			%end
		</div>
	</main>

</body>
<script src="../static/js/addNewCompany.js"></script>
</html>
