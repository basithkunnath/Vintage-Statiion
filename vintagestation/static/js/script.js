// Navbar

let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () => {
  menuIcon.classList.toggle('bx-x');
  navbar.classList.toggle('active');
};

let sections = document.querySelectorAll('section');
let navlinks = document.querySelectorAll('header nav a');

window.onscroll = () => {
  sections.forEach(sec => {
    let top = window.scrollY;
    let offset = sec.offsetTop - 150;
    let height = sec.offsetHeight;
    let id = sec.getAttribute('id');

    if (top >= offset && top < offset + height) {
      navlinks.forEach(links => {
        links.classList.remove('active');
        document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
      });
    }
  });

  // Navbar sticky class toggle
  let header = document.querySelector('header');
  header.classList.toggle('sticky', window.scrollY > 100);

  menuIcon.classList.remove('bx-x');
  navbar.classList.remove('active');
};



// Highlight navbar active

document.addEventListener("DOMContentLoaded", function() {
    // Get current URL path
    var currentPath = window.location.pathname;
    
    // Get all nav links
    var navLinks = document.querySelectorAll(".navbar a");
    
    navLinks.forEach(function(link) {
        // Check if link's href matches the current path
        if(link.getAttribute("href") === currentPath) {
            // Remove "active" class from any previously active link
            navLinks.forEach(function(item) {
                item.classList.remove("active");
            });
            // Add "active" class to the current link
            link.classList.add("active");
        }
    });
});









// Display the first tab by default
document.addEventListener("DOMContentLoaded", function() {
    document.querySelector(".tab-link").click();
});


// Cart 

document.addEventListener('DOMContentLoaded', () => {
    const decreaseButtons = document.querySelectorAll('.decrease');
    const increaseButtons = document.querySelectorAll('.increase');
    const quantityNumbers = document.querySelectorAll('.quantity-number');
    const removeButtons = document.querySelectorAll('.remove');

    decreaseButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            let quantity = parseInt(quantityNumbers[index].innerText);
            if (quantity > 1) {
                quantityNumbers[index].innerText = quantity - 1;
            }
        });
    });

    increaseButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            let quantity = parseInt(quantityNumbers[index].innerText);
            quantityNumbers[index].innerText = quantity + 1;
        });
    });

    removeButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            button.parentElement.parentElement.remove();
        });
    });
});


// Signup

document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirmPassword').value;
    
    if (password !== confirmPassword) {
        alert('Passwords do not match.');
    } else {
        alert('Signup successful!');
        // Here you would typically send the data to the server
    }
});



// logout Popup

function openModal() {
    document.getElementById("logoutModal").style.display = "flex";
}

function closeModal() {
    document.getElementById("logoutModal").style.display = "none";
}

function logout() {
    // Add your logout logic here
    alert("You have been logged out.");
    closeModal();
}



