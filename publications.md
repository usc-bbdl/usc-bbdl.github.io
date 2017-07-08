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
.paper_authors {font-size: 12px; color: '#e8e8e8'; text-align: justify;
    text-justify: inter-word; float:'left'}
.paper_author_p {margin-bottom:0px; padding:0px; width: 100%}
.journal_info {font-size: 10px; color: '#fff000'}
.publication_card {padding-top: 5px; padding-bottom: 0px; margin-top: 10px; margin-bottom:2px}
.article_title {font-size: 18px; font-weight: bold; font-style: normal; font-weight: 300;    text-align: justify;
    text-justify: inter-word;}
.btn {float:'right'; border: 1px solid #f4f5f7; background-color:#f4f5f7; padding-left:0; padding-right:0; color: #b9c1ce}
</style>


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

<div>
{% for paper in site.data.publications %}
  <div class="publication_card">
    <a class="article_title" href="./{{paper.Link}}" title="{{paper.Abstract}}">{{paper.Title}}</a>
  </div>
  <div class="paper_author_p">
    <span class="paper_authors">{{paper.Author | upcase}}</span>
    <br>
    <button class="btn" data-clipboard-text="{{paper.BibTex}}">
      BIBTEX
    </button>
    </div>

{% endfor %}

</div>
