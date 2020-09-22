		document.addEventListener("DOMContentLoaded", function() {



			document.querySelector("#num-price").innerHTML = '{{ result.price }}';
			selected_price = undefined;

			document.querySelectorAll('input[type="radio"]').forEach(function(button) {
				document.querySelector("#num-price").innerHTML = '{{ result.small }}';
				selected_price = '{{ result.small }}';
				button.onchange = function() {
					if (button.value == "small") {
						document.querySelector('#num-price').innerHTML = '{{ result.small }}';
						selected_price = '{{ result.small }}';
					}
					if (button.value == "large") {
						document.querySelector('#num-price').innerHTML = '{{ result.large }}';
						selected_price = '{{ result.large }}';
					}

					calculate_adds();
				}
			})

			document.querySelectorAll('#add-select').forEach(function(button) {
				button.onchange = calculate_adds;
			})

		})


		function calculate_adds() {
			price = parseFloat(selected_price);
			document.querySelectorAll('#add-select').forEach(function(button) {
				if (button.value != 1) {
					price = price + 0.5;
				}
			})
			document.querySelector('#num-price').innerHTML = price;
		}