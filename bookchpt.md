---
layout: page
title: Book Chapters
permalink: /bookchpt/
menu: main2
---

<div>
<button onclick="window.location.href='../publications/';">Publications</button>
<button onclick="window.location.href='../fulllengthpeerreviewedabstracts/';">Full-Length Peer-Reviewed Abstracts</button>
<button onclick="window.location.href='../peerreviewedabstracts/';">Peer-Reviewed Abstracts</button>
<button onclick="window.location.href='../abstracts/';">Abstracts</button>
<button onclick="window.location.href='../bookchpt/';">Book Chapters</button>
<button onclick="window.location.href='../invitedsymposia/';">Invited Symposia</button>
<button onclick="window.location.href='../dissertation_theses/';">Dissertations & Theses</button>
</div>

<head>
  <style>
#myBtn {
    display: none; /* Hidden by default */
    position: fixed; /* Fixed/sticky position */
    bottom: 20px; /* Place the button at the bottom of the page */
    right: 30px; /* Place the button 30px from the right */
    z-index: 99; /* Make sure it does not overlap */
    border: none; /* Remove borders */
    outline: none; /* Remove outline */
    background-color: #9b4343; /* Set a background color */
    color: white; /* Text color */
    cursor: pointer; /* Add a mouse pointer on hover */
    padding: 15px; /* Some padding */
    border-radius: 10px; /* Rounded corners */
}

#myBtn:hover {
    background-color: #555; /* Add a dark-grey background on hover */
}
    
  </style>
</head>
<body>
<br>
  
<h1 style="font-size:40px;">Years</h1>

<div>
<button onclick="window.location.href='#2014';">2014</button>
<button onclick="window.location.href='#2013';">2013</button>
<button onclick="window.location.href='#2009';">2009</button>
<button onclick="window.location.href='#2006';">2006</button>
</div>

<br>
  
<h1 style="font-size:40px;" id="2018">2014</h1>

Inouye JM, Kutch JJ, and Valero-Cuevas FJ.<br>
<b><a href="../Papers/InouyeRSS.pdf">
"Optimizing the Topology of Tendon-Driven Fingers: Rationale, Predictions and Implementation."</a></b><br>
in The Human Hand: A Source of Inspiration for Robotic Hands, Springer Tracts in Advanced Robotics (STAR) series, Balasubramanian, R. and Santos, V.J., Eds., Springer, Heidelberg, 95: p.247-266, 2014.<br>


<br>

<h1 style="font-size:40px;" id="2013">2013</h1>

Valero-Cuevas FJ.<br>
<b>
"The Human Hand as an Inspiration for Robot Hand Development."</b><br>
in The Human Hand: A Source of Inspiration for Robotic Hands, Springer Tracts in Advanced Robotics (STAR) series, Balasubramanian, R. and Santos, V.J., Eds., Springer, Heidelberg, 2013.<br>

<br>

<h1 style="font-size:40px;" id="2009">2009</h1>

Valero-Cuevas FJ.<br>
<b><a href="../Papers/Valero-Cuevas_PMC_V_Intro.pdf">
"Why the hand?"</a></b><br>
Advances in Experimental Medicine and Biology, 629: p.553-7, 2009.<br>

<br>

Valero-Cuevas FJ.<br>
<b><a href="../Papers/ValeroCuevas2_PMC_V_Chapter.pdf">
"A mathematical approach to the mechanical capabilities of limbs and fingers."</a></b><br>
Advances in Experimental Medicine and Biology, 629: 619-633, 2009.<br>

<br>

<h1 style="font-size:40px;" id="2006">2006</h1>

Chang J, Valero-Cuevas FJ, Hentz VR, and Chase R.<br>
<b>
"Anatomy and Biomechanics of the hand."</b><br>
Atlas of Plastic Surgery. Hentz VR and Chase R, editors, 2006.<br>


<button onclick="topFunction()" id="myBtn" title="Go to top">Top</button>
<!-- scroll to top button -->
<script>
 // When the user scrolls down 20px from the top of the document, show the button
 window.onscroll = function() {scrollFunction()};

 function scrollFunction() {
     if (document.body.scrollTop > 400 || document.documentElement.scrollTop > 20) {
         document.getElementById("myBtn").style.display = "block";
     } else {
         document.getElementById("myBtn").style.display = "none";
     }
 }

 // When the user clicks on the button, scroll to the top of the document
 function topFunction() {
     document.body.scrollTop = 0; // For Chrome, Safari and Opera
     document.documentElement.scrollTop = 0; // For IE and Firefox
 }
</script>
</body>
<!-- scroll to top button -->



<!--
<head>
<link rel="stylesheet" href="s://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css">
<script src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
<script src="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
<style>
th
{
border-bottom: 1px solid #d6d6d6;
}
tr:nth-child(even)
{
background:#e9e9e9;
}
</style>
</head>

<body>

<div data-role="page" id="pageone">
  <div data-role="header">
    <h1>Book chapters</h1>
  </div>
  
  <div data-role="main" class="ui-content">
    
    <table data-role="table" data-mode="columntoggle" class="ui-responsive ui-shadow" id="myTable" data-filter="true" data-input="#filterTable-input">
      <thead>
        <tr>
          <th>Citation</th>
          <th data-priority="1">PDF</th>
          <th data-priority="2">Supplemental Materials</th>
          <th data-priority="3">Year</th>
        </tr>
      </thead>

      <tbody>

        <tr>
          <td>Valero-Cuevas FJ.<br>
              <b>"The Human Hand as an Inspiration for Robot Hand Development."</b> <br>
              in The Human Hand: A Source of Inspiration for Robotic Hands, Springer Tracts in Advanced Robotics (STAR) series, Balasubramanian, R. and Santos, V.J., Eds., Springer, Heidelberg. In press, 2013.</td>
          <td></td>
          <td></td>
          <td>2013</td>
        </tr>

        <tr>
          <td>Inouye JM, Kutch JJ, and Valero-Cuevas FJ. <br>
              <b>Optimizing the Topology of Tendon-Driven Fingers: Rationale, Predictions and Implementation.</b> <br>
              in The Human Hand: A Source of Inspiration for Robotic Hands, Springer Tracts in Advanced Robotics (STAR) series, Balasubramanian, R. and Santos, V.J., Eds., Springer, Heidelberg. In press.</td>
          <td><a href="https://usc-bbdl.github.io/Papers/InouyeRSS.pdf">Link</a></td>
          <td></td>
          <td>2014</td>
        </tr>

        <tr>
          <td>Valero-Cuevas FJ.<br>
              <b>Why the hand?</b> <br>
              Advances in Experimental Medicine and Biology, 629: p.553-7, 2009.</td>
          <td><a href="https://usc-bbdl.github.io/Papers/Valero-Cuevas_PMC_V_Intro.pdf">Link</a></td>
          <td></td>
          <td>2009</td>
        </tr>

        <tr>
          <td>Valero-Cuevas FJ.<br>
              <b>A mathematical approach to the mechanical capabilities of limbs and fingers.</b> <br>
              Advances in Experimental Medicine and Biology, 629: 619-633, 2009.</td>
          <td><a href="https://usc-bbdl.github.io/Papers/ValeroCuevas2_PMC_V_Chapter.pdf">Link</a></td>
          <td></td>
          <td>2009</td>
        </tr>

        <tr>
          <td>Chang J, Valero-Cuevas FJ, Hentz VR, and Chase R.<br>
              <b>Anatomy and Biomechanics of the hand.</b> <br>
              Atlas of Plastic Surgery. Hentz VR and Chase R, editors.</td>
          <td></td>
          <td></td>
          <td>2006</td>
        </tr>

        </tbody>
        </table>
  </div>

  <div data-role="footer">
    <h1>USC BBDL</h1>
  </div>
</div>
-->
