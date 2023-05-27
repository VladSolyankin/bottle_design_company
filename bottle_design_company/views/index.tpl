<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport"
	      content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<link rel="stylesheet" href="../static/css/index.css">
	<script src="../js/index.js"></script>
	<title>Design Company</title>
</head>
<body>
	<header class="index__header">
		<a href="index.html">
			<img src="./static/images/logo.png" alt="Design Company logo" class="header__logo">
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

	<div class="index__hero">
		<span class="hero__text">Welcome to<br>our Design Site!</span>
	</div>

	<main id="main">
		<div class="main__cards">
			<div class="main__card bg-red">
				<div class="card__icon"><img src="./static/images/click.png" alt=""></div>
				<span><b style="font-size: 24px">Responsive</b></span>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dicta, maxime!</p>
			</div>
			<div class="main__card bg-teal">
				<div class="card__icon"><img src="./static/images/device.png" alt=""></div>
				<span><b style="font-size: 24px">Easy to use</b></span>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias, quo.</p>
			</div>
			<div class="main__card bg-yellow">
				<div class="card__icon"><img src="./static/images/fast.png" alt=""></div>
				<span><b style="font-size: 24px">Quick Support</b></span>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi, velit.</p>
			</div>
		</div>

		<div class="main__info">
			<div class="info__image"></div>
			<div class="info__text">
				<h2 style="font-size: 24px; margin-bottom: 2vh">Startup Business</h2>
				<p class="text__p">Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet. Dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet.<br><br>Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet. Dolore magna aliquam erat volutpat.</p>
				<button class="info__button"><a href="#projects">LEARN MORE</a></button>
			</div>
		</div>
	</main>

	<div class="main__projects" id="projects">
		<h2 style="font-size: 26px">Recent Projects</h2>
		<p class="text__p" style="font-size: 24px">Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh <br> euismod tincidunt ut laoreet. Dolore magna aliquam erat volutpat.</p>
		<div class="projects__images">
			<div class="images__row-1">
				<div class="images__grid-1"></div>
				<div class="images__grid-2"></div>
				<div class="images__grid-3"></div>
			</div>
			<div class="images__row-2">
				<div class="images__grid-4"></div>
				<div class="images__grid-5"></div>
				<div class="images__grid-6"></div>
				<div class="images__grid-7"></div>
			</div>
		</div>
		<button class="view_button">View more</button>
	</div>

	<div class="contact__information">
		<div class="information__contacts">
			<img src="./static/images/logo.png" alt="" style="margin-top: -2vh">
			<ul>
				<li>123-456-789-0</li>
				<li>design_company@mail.com</li>
				<li>www.designcompany.com</li>
			</ul>
		</div>
		<div class="information__links">
			<h2>Useful links</h2>
			<ul>
				<li>HTML&CSS</li>
				<li>BOOTSTRAP</li>
				<li>JQUERY</li>
				<li>REACTJS</li>
			</ul>
		</div>
		<div class="information__newsletter">
			<h2>Newsletter</h2>
			<p>Lorem ipsum dolor sit amet,<br> consectetur adipisicing elit. Aliquid, consectetur dolorem<br>et officiis quia ullam!</p>
			<label>
				<input type="email" placeholder="Email" class="input__email">
				<button class="info__button">Submit</button>
			</label>
		</div>
	</div>

	<div class="footer">
		Lab #2<br>GUAP
	</div>

</body>
</html>