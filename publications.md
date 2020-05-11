---
layout: page
title: Publications
permalink: /publications/
menu: main
---
<a>
<select onchange="javascript:if (this.options[this.selectedIndex].value != '') window.location.href=this.options[this.selectedIndex].value;this.options[0].selected;" style="width:300px;font-size:16px;border:none;-webkit-appearance:none; color: 'blue'" >
<option value="">Click here for Extended Publications</option>
<option value="../fulllengthpeerreviewedabstracts/">Full-Length Peer-Reviewed Abstracts</option>
<option value="../peerreviewedabstracts/">Peer-Reviewed Abstracts</option>
<option value="../abstracts/">Abstracts</option>
<option value="../bookchpt/">Book Chapters</option>
<option value="../invitedsymposia/">Invited Symposia</option>
<option value="../dissertation_theses/">Dissertations & Theses</option>
</select>
</a>

<!-- Clipboard copier -->
<script async src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/1.7.1/clipboard.min.js"></script>
<script src="../publication_tags.js"></script>

<link rel="stylesheet" type="text/css" media="screen" href="../css/styles.css" />
<div>
<div class="yearbuttons">
{% for year_of_interest in (1997..2020) reversed %}
  <a class="year_button_container" href="#{{year_of_interest}}">
    <button class="year_button">{{year_of_interest}}</button>
  </a>
  {% endfor %}
</div>
  <br>
<h3>Topics</h3>

<button onclick="showAll()">Show All</button>
<button onclick="showOnly('.neuroscience')">Neuroscience</button>
<button onclick="showOnly('.computation_and_modeling')">Computation and Modeling</button>
<button onclick="showOnly('.robotics')">Robotics</button>
<button onclick="showOnly('.clinical_research')">Clinical Research</button>
<button onclick="showOnly('.biomechanics')">Biomechanics</button>
<button onclick="showOnly('.manipulation')">Manipulation</button>
<br>
<button onclick="topFunction()" id="myBtn" title="Go to top">Top</button>
</div>
<!-- make sure the max date is the current year! -->
{% for year_of_interest in (1997..2020) reversed %}

  {% comment %} casting an integer to a string {% endcomment %}
  {% assign yearAsString = year_of_interest | append:"" %}
  <div class='year_header_container'>
  <large_year id="{{year_of_interest}}">{{year_of_interest}}</large_year>
  <div>

  {% comment %} filtering datas {% endcomment %}
  {% assign selectedEntries = site.data.publications | where: "Year", yearAsString %}
  {% for paper in selectedEntries %}
             <div class="publication_card {{paper.Tags}}" >
             <div class="paper_author_container">
               {{paper.Author}} <a class="article_title" href="../../{{paper.Link}}" 
               target="_blank"
               title="{{paper.Abstract}}">{{paper.Title}}</a> <i>{{paper.Journal}}</i>, {{paper.Year}} <br>
                 <button class="btn" data-clipboard-text="{{paper.BibTex}}">Copy BibTex</button>
             </div>
             </div>
     {% endfor %}
 {% endfor %}

 <script>
 window.onload = function(){
   var clipboard = new Clipboard('.btn');
   clipboard.on('success', function(e) {
       console.log(e);
       console.log("Copied to Clipboard");
   });
   clipboard.on('error', function(e) {
       console.log(e);
   });
 }
 </script>

 <!-- end Clipboard copier -->
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
 <!-- scroll to top button -->
