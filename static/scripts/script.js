$(document).ready(function(){
	
	// Initially hide Advance Search box
	$(".adv-search").hide();

	// Advance search box toggle when Advance search button clicked
	$(".adv-search-btn").click(function(){
		$(".adv-search").toggle();
	});

	// if search box form left empty
	$('#search-form').submit(function(){
		if($.trim($("#searchInput").val())===""){
			alert("You did not fill out Location");
			return false;
		}
	});

	//check if Location or Bedroom field is empty
	$('#adv-search-form').submit(function(){
		if($.trim($("#location").val())==="" || $.trim($("#bedrooms").val())==="" ){
			alert("You did not fill out Location or Bedrooms");
			return false;
		}
	});

	//Check the database and populate the locations
	var loc=[];
	function loadCountries(){
		$.getJSON('/check',function(data,status,xhr){
			for (var i = 0; i<data.length;i++){
				loc.push(data[i].Location);

			}
		});
	};

	loadCountries();
	
	$("#location,#searchInput").autocomplete({
		source: loc,
		select: function(event,ui){
			$("#location,#searchInput").val(ui.item.Location);
		}
	});

});
































