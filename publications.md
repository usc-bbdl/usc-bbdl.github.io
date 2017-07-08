---
layout: page
title: Publications
permalink: /publications/
menu: main
---
<!-- Clipboard copier -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/1.7.1/clipboard.min.js"></script>
<script>
var clipboard = new Clipboard('.btn');
clipboard.on('success', function(e) {
    console.log(e);
    console.log("Copied to Clipboard");
});
clipboard.on('error', function(e) {
    console.log(e);
});
</script>

<!-- end Clipboard copier -->



<style>
.paper_authors {font-size: 12px; color: '#e8e8e8'}
.paper_author_p {margin-bottom:0px; padding:0px; width: 100%}
.journal_info {font-size: 10px; color: '#fff000'}
.publication_card {padding-top: 5px; padding-bottom: 5px; margin-top: 10px; margin-bottom:10px}
.article_title {font-size: 18px; font-weight: bold; font-style: normal; font-weight: 300;}
</style>


<a>
    <select onchange="javascript:if (this.options[this.selectedIndex].value != '') window.location.href=this.options[this.selectedIndex].value;this.options[0].selected;" style="width:300px;font-size:16px;border:none;-webkit-appearance:none; color: 'blue'" >
        <option value="">Click here for Extended Publications</option>
        <option value="https://usc-bbdl.github.io/fulllengthpeerreviewedabstracts/">Full-Length Peer-Reviewed Abstracts</option>
        <option value="https://usc-bbdl.github.io/peerreviewedabstracts/">Peer-Reviewed Abstracts</option>
        <option value="https://usc-bbdl.github.io/abstracts/">Abstracts</option>
        <option value="https://usc-bbdl.github.io/bookchpt/">Book Chapters</option>
        <option value="https://usc-bbdl.github.io/invitedsymposia/">Invited Symposia</option>
        <option value="https://usc-bbdl.github.io/dissertation_theses/">Dissertations & Theses</option>
    </select>
  </a>

<div>
{% for paper in site.data.publications %}
  <div class="publication_card">
    <a class="article_title" href="./{{paper.Link}}" title="{{paper.Abstract}}">{{paper.Title}}</a>
  </div>
  <div class="paper_author_p">
    <span class="paper_authors">{{paper.Author | upcase}}</span>
    </div>
  <button class="btn" data-clipboard-text="{{paper.BibTex}}">
    Copy BibTex
  </button>
{% endfor %}

</div>
