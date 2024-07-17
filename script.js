// Function to handle form submission
function handleFormSubmit(event) {
    event.preventDefault(); // Prevent default form submission
    
    // Fetch form data
    const formData = new FormData(event.target);
    const name = formData.get('name');
    const email = formData.get('email');
    const message = formData.get('message');
    
    // Example: Validate and process form data
    if (name && email && message) {
      // Simulate sending data to server (replace with actual API call)
      setTimeout(() => {
        alert('Message sent successfully!');
        event.target.reset(); // Clear form fields after submission
      }, 1000); // Simulate delay
    } else {
      alert('Please fill out all fields.');
    }
  }
  
  // Event listener for form submission
  document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', handleFormSubmit);
  });
  
  // Example of adding a click event to a button
  const btn = document.querySelector('.btn');
  btn.addEventListener('click', function() {
    alert('Button clicked!');
  });
  