$(function() {

  var writeToPage = function(inArray, targetElem) {
    var elemId = "#" + targetElem;
    var targetDOM = $(elemId);
    for (var i = 0; i < inArray.length; i++) {
      targetDOM.append("<li>" + String(inArray[i]) + "</li>");
    }
  }



  $.ajax({
  url: '../countries.json',
  type: 'get',
  dataType: 'json',
  error: function(data){
  },
  success: function(data){

/////////////////// INSECTS/ARTHROPODS

      // Filter for all beetles!    
      var coleo = [];
      data.map(function(d) {
        if (d["group"].toLowerCase() == "beetles") {
          coleo.push("<i>"+d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      coleo = coleo.sort();
      writeToPage(coleo, "coleo");

      var leps = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "moths & butterflies") {
          // add them to the list
          leps.push("<i>"+d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      leps = leps.sort();

      writeToPage(leps, "leps");

/////// flies
      var dipter = [];

      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "flies") {
          // add them to the list
          dipter.push("<i>"+d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      dipter = dipter.sort();

      writeToPage(dipter, "dipter");


      var hemi = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "true bugs") {
          // add them to the list
          hemi.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      hemi = hemi.sort();

      writeToPage(hemi, "hemi");

   // crickets & grasshoppers
      var othro = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "crickets & grasshoppers") {
          // add them to the list
          othro.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      othro = othro.sort();

      writeToPage(othro, "othro");

   // Ants, Bees, & Wasps
      var hymenopt = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "ants, bees & wasps") {
          // add them to the list
          hymenopt.push("<i>"+d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      hymenopt = hymenopt.sort();

      writeToPage(hymenopt, "hymenopt");

   // Dragonflies & Mayflies
      var odon = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "dragonflies & mayflies") {
          // add them to the list
          odon.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      odon = odon.sort();

      writeToPage(odon, "odon");

    // All other insects
      var otherIns = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "other insects") {
          // add them to the list
          otherIns.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      otherIns = otherIns.sort();

      writeToPage(otherIns, "otherIns");    

    // Spiders
      var spiders = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "spiders") {
          // add them to the list
          spiders.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      spiders = spiders.sort();

      writeToPage(spiders, "spiders");  



// Mites & Ticks
      var acari = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "mites & ticks") {
          // add them to the list
          acari.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      acari = acari.sort();

      writeToPage(acari, "acari");  


// Other Arachnids
      var otherArach = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "other arachnids") {
          // add them to the list
          otherArach.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      otherArach = otherArach.sort();

      writeToPage(otherArach, "otherArach");  

// Other Arthropods
      var otherArthro = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "other arthropods") {
          // add them to the list
          otherArthro.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      otherArthro = otherArthro.sort();

      writeToPage(otherArthro, "otherArthro"); 

//////////////BIRDS/////////////////////////////////////////////

// ducks, geese & relatives
      var ducks = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "ducks, geese & relatives") {
          // add them to the list
          ducks.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      ducks = ducks.sort();

      writeToPage(ducks, "ducks"); 


// Falcons, Eagles & Buzzards
      var falcons = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "falcons, eagles & buzzards") {
          // add them to the list
          falcons.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      falcons = falcons.sort();

      writeToPage(falcons, "falcons"); 

// Fowl & Quail
      var fowl = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "fowl & quail") {
          // add them to the list
          fowl.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      fowl = fowl.sort();

      writeToPage(fowl, "fowl"); 

// Perching Birds
      var perch = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "perching birds") {
          // add them to the list
          perch.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      perch = perch.sort();

      writeToPage(perch, "perch"); 


// Owls
      var owls = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "owls") {
          // add them to the list
          owls.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      owls = owls.sort();

      writeToPage(owls, "owls"); 


// Other Birds
      var otherBirds = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "other birds") {
          // add them to the list
          otherBirds.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      otherBirds = otherBirds.sort();

      writeToPage(otherBirds, "otherBirds"); 

//////////////MAMMALS/////////////////////////////////////////////

//  Pigs & Deer 
      var pigsDeer = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "pigs & deer") {
          // add them to the list
          pigsDeer.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      pigsDeer = pigsDeer.sort();

      writeToPage(pigsDeer, "pigsDeer"); 

//  Bats 
      var bats = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "bats") {
          // add them to the list
          bats.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      bats = bats.sort();

      writeToPage(bats, "bats"); 

// Rabbits, & Hares
      var rabbit = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "rabbits, & hares") {
          // add them to the list
          rabbit.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      rabbit = rabbit.sort();

      writeToPage(rabbit, "rabbit"); 

// Rodents
      var rodents = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "rodents") {
          // add them to the list
          rodents.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      rodents = rodents.sort();

      writeToPage(rodents, "rodents"); 

// Other Mammals
      var otherMam = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "other mammals") {
          // add them to the list
          otherMam.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      otherMam = otherMam.sort();

      writeToPage(otherMam, "otherMam"); 

//////////////MAMMALS/////////////////////////////////////////////

//  Lizards 
      var lizards = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "lizards") {
          // add them to the list
          lizards.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      lizards = lizards.sort();

      writeToPage(lizards, "lizards"); 

//  Snakes 
      var snakes = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "snakes") {
          // add them to the list
          snakes.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      snakes = snakes.sort();

      writeToPage(snakes, "snakes"); 

//  STurtles & Tortoises 
      var turt = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "turtles & tortoises") {
          // add them to the list
          turt.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      turt = turt.sort();

      writeToPage(turt, "turt"); 

//  Other Reptiles
      var otherRep = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "other reptiles") {
          // add them to the list
          otherRep.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      otherRep = otherRep.sort();

      writeToPage(otherRep, "otherRep"); 


// ///////AMPHIBIANS

//  Frogs & Toads
      var frogs = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "frogs & toads") {
          // add them to the list
          frogs.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      frogs = frogs.sort();

      writeToPage(frogs, "frogs");       

//  Salamanders
      var sals = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "salamanders") {
          // add them to the list
          sals.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      sals = sals.sort();

      writeToPage(sals, "sals"); 

//  Other Amphibians
      var otherAmp = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "other amphibians") {
          // add them to the list
          otherAmp.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      otherAmp = otherAmp.sort();

      writeToPage(otherAmp, "otherAmp"); 

/////////////////////////// VASC PLANTS ////////////////////////

//  Ferns & Horsetails 
      var ferns = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "ferns & horsetails ") {
          // add them to the list
          console.log(d["key"])
          ferns.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      ferns = ferns.sort();
      console.log(ferns)

      writeToPage(ferns, "ferns");    


//  Conifers
      var conifers = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "conifers") {
          // add them to the list
          conifers.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      conifers = conifers.sort();

      writeToPage(conifers, "conifers");    

//  Coontails
      var coontails = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "coontails") {
          // add them to the list
          coontails.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      coontails = coontails.sort();

      writeToPage(coontails, "coontails");    

//  Grasses & related flowering plants
      var grass = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "grasses & related flowering plants") {
          // add them to the list
          grass.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      grass = grass.sort();

      writeToPage(grass, "grass");  

//  Other vascular plants
      var otherVas = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "other vascular plants") {
          // add them to the list
          otherVas.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      otherVas = otherVas.sort();

      writeToPage(otherVas, "otherVas"); 

//  Mosses, Hornworts & Liverworts
      var moss = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "mosses, hornworts & liverworts") {
          // add them to the list
          moss.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      moss = moss.sort();

      writeToPage(moss, "moss"); 

//  Algae
      var algae = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "algae") {
          // add them to the list
          algae.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      algae = algae.sort();

      writeToPage(algae, "algae"); 

  //  All other plants 
      var otherPlants = [];
      // find all that match that group name
      data.map(function(d) {
        if (d["group"].toLowerCase() == "all other plants") {
          // add them to the list
          otherPlants.push("<i>"+ d["key"] + "</i>: " + d["value"]+" observation(s)");
        }
      });
      // sort the list
      otherPlants = otherPlants.sort();

      writeToPage(otherPlants, "otherPlants");     
    }
  });
});