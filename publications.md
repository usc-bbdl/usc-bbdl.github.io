---
layout: page
title: Publications
permalink: /publications/
menu: main
---

<!-- Clipboard copier -->
<script async src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/1.7.1/clipboard.min.js"></script>





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
.paper_authors {
  font-size: 0.6em;
  color: #b9c1ce;
  text-align: justify;
  text-justify: inter-word;
  float:'left'
}
.paper_author_container {margin-bottom:0px; padding:0px; width: 100%}
.journal_info {font-size: 0.6em; color: #b9c1ce}
.publication_card {
  padding-top: 5px;
  text-justify: inter-word;
  padding-bottom: 0px;
  margin-top: 10px;
  margin-bottom:2px
}
.article_title {font-size: 1em; font-weight: bold; font-style: normal; font-weight: 300;    text-align: justify;
    text-justify: inter-word;}
.btn {float:'right'; border: 1px solid #f4f5f7; background-color:#f4f5f7; padding-left:0; padding-right:0; color: #b9c1ce}
large_year {
  font-size: 3em;
  font-weight:600;
}
.year_button {
    box-shadow: 0 0 0 1px #767676 inset!important;
    color: #767676!important;
    margin-bottom: 0.75em;
    font-weight: 400;
    border-radius: .28571429rem;
    text-transform: none;
    font-size: 0.7rem;
    user-select: none;
    line-height: 1em;
    -webkit-tap-highlight-color: transparent;
    font-style: normal;
    transition: opacity .1s ease,background-color .1s ease,color .1s ease,box-shadow .1s ease,background .1s ease;
    text-align: center;
    text-decoration: none;
    text-shadow: none!important;
    cursor: pointer;
    display: inline-block;
    min-height: 1em;
    margin-bottom: 0.2rem;
    width:50px;
    padding-top: 0.5em;
    padding-right: 1em;
    padding-bottom: 0.5em;
    padding-left: 1em;
    outline: 0;
    border: none;
    vertical-align: baseline;
    background: transparent none!important;
}
.year_button_container:hover {
    text-decoration:none;
}
</style>


<div class="yearbuttons">
{% for year_of_interest in (1997..2017) reversed %}
  <a class="year_button_container" href="#{{year_of_interest}}">
    <button class="year_button">{{year_of_interest}}</button>
  </a>
  {% endfor %}
</div>

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

<!-- scroll to top button -->
<button onclick="topFunction()" id="myBtn" title="Go to top">Top</button>
<!-- end scroll to top button -->

{% for year_of_interest in (1997..2017) reversed %}

  {% comment %} casting an integer to a string {% endcomment %}
  {% assign yearAsString = year_of_interest | append:"" %}
  <div class='year_header_container'>
  <large_year id="{{year_of_interest}}">{{year_of_interest}}</large_year>
  <div>

  {% comment %} filtering datas {% endcomment %}
  {% assign selectedEntries = site.data.publications | where: "Year", yearAsString %}
  {% for paper in selectedEntries %}
             <div class="publication_card">
               <a class="article_title" href="../../{{paper.Link}}" title="{{paper.Abstract}}">{{paper.Title}}</a>
             </div>
             <div class="paper_author_container">
               <div class="paper_authors">{{paper.Author | upcase}}</div>
               <div class="journal_info">{{paper.Year}}—{{paper.Journal | upcase}}
                 <button class="btn" data-clipboard-text="{{paper.BibTex}}">
                   BIBTEX
                 </button>
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
