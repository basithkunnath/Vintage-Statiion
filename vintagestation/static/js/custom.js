(function () {
	'use strict';

	var tinyslider = function () {
		var el = document.querySelectorAll('.testimonial-slider');

		if (el.length > 0) {
			var slider = tns({
				container: '.testimonial-slider',
				items: 1,
				axis: "horizontal",
				controlsContainer: "#testimonial-nav",
				swipeAngle: false,
				speed: 700,
				nav: true,
				controls: true,
				autoplay: true,
				autoplayHoverPause: true,
				autoplayTimeout: 3500,
				autoplayButtonOutput: false
			});
		}
	};
	tinyslider();




	var sitePlusMinus = function () {

		var value,
			quantity = document.getElementsByClassName('quantity-container');

		function createBindings(quantityContainer) {
			var quantityAmount = quantityContainer.getElementsByClassName('quantity-amount')[0];
			var increase = quantityContainer.getElementsByClassName('increase')[0];
			var decrease = quantityContainer.getElementsByClassName('decrease')[0];
			increase.addEventListener('click', function (e) { increaseValue(e, quantityAmount); });
			decrease.addEventListener('click', function (e) { decreaseValue(e, quantityAmount); });
		}

		function init() {
			for (var i = 0; i < quantity.length; i++) {
				createBindings(quantity[i]);
			}
		};

		function increaseValue(event, quantityAmount) {
			value = parseInt(quantityAmount.value, 10);

			console.log(quantityAmount, quantityAmount.value);

			value = isNaN(value) ? 0 : value;
			value++;
			quantityAmount.value = value;
		}

		function decreaseValue(event, quantityAmount) {
			value = parseInt(quantityAmount.value, 10);

			value = isNaN(value) ? 0 : value;
			if (value > 0) value--;

			quantityAmount.value = value;
		}

		init();

	};
	sitePlusMinus();


})()


document.getElementById('show-register').addEventListener('click', function (event) {
	event.preventDefault();
	document.getElementById('register-box').style.display = 'block';
	document.querySelector('.form-box').style.display = 'none';
});

document.getElementById('show-login').addEventListener('click', function (event) {
	event.preventDefault();
	document.querySelector('.form-box').style.display = 'block';
	document.getElementById('register-box').style.display = 'none';
});


document.addEventListener("DOMContentLoaded", function () {
	const menuIcon = document.querySelector('#menu-icon');
	const navbar = document.querySelector('.navbar');
	const navlinks = document.querySelectorAll('header nav a');
	const header = document.querySelector('header');
	const sections = document.querySelectorAll('section');

	// Toggle navbar visibility on menu icon click
	menuIcon.onclick = () => {
		menuIcon.classList.toggle('bx-x');
		navbar.classList.toggle('active');
	};

	// Function to handle scroll events
	window.onscroll = () => {
		let scrollPos = window.scrollY;

		// Sticky navbar toggle
		header.classList.toggle('sticky', scrollPos > 100);

		// Highlight the active section link in the navbar
		sections.forEach(sec => {
			let top = scrollPos;
			let offset = sec.offsetTop - 150;
			let height = sec.offsetHeight;
			let id = sec.getAttribute('id');

			if (top >= offset && top < offset + height) {
				navlinks.forEach(link => {
					link.classList.remove('active');
					document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
				});
			}
		});
	};

	// Close the navbar when a link is clicked
	navlinks.forEach(link => {
		link.addEventListener('click', () => {
			menuIcon.classList.remove('bx-x');
			navbar.classList.remove('active');
		});
	});
});