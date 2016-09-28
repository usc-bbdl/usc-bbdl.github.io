---
layout: page
title: Chapter 4
---
# Chapter 4: Tendon-Driven Limbs  (*under construction*)

*Last updated Dec. 26 2015 by Francisco Valero-Cuevas*


**Abstract:**

_________


The purpose of this chapter is to introduce you to the fundamentals of *tendon-driven limbs*, and to begin to explore how they affect our understanding of vertebrate and robotic limbs. Many robotic limbs are driven by motors or pistons that act on the kinematic degrees of freedom (DOFs, e.g., rotational joints) either via linkages, cables, or gears. These actuators can exert forces and torques in both clock- wise and counterclockwise directions, symmetrically in either direction—which in the robotics literature are idealized and analyzed as *torque-driven limbs*. The term ‘tendon-driven’ comes from the robotics literature where limbs are actuated via a variety of motors or muscles that pull on strings, cables, or tendons that cross the kinematic DOFs. Thus, these actuators can only pull on, or resist stretch in, the tendons. But they cannot not push on the tendons. This discontinuity and asymmetry in actuation makes tendon-driven limbs distinctly different from their torque-driven counterparts with symmetric actuation. While this asymmetric actuation in tendon-driven limbs might have some mechanical disadvantages and complicate their analysis, it can also have advantages such as being light weight, and allowing remote actuation and flexibility of tendon routing. As the reader will discover, varying tendon routings and moment arms can enable multiple solutions for specific functional requirements, especially when size and power constraints are critical. More importantly, because the nervous system is unavoidably confronted with the need to actuate and control the tendon-driven limbs in vertebrates, the nuances of tendon-driven limbs provide insights into the nature of neural control, evolutionary adaptations, disability, and rehabilitation that is not available in the torque-driven formulation. Note that throughout this book, I use the terms muscle when relating specifically to the behavior, forces, or state of the muscle tissue, musculotendon when relating to issues that involve the muscle and its tendons of origin and insertion, and tendon when relating specifically to the behavior, forces, or state of the tendon of insertion of the muscle. For most mathematical and mechanical analyses, however, the term tendon suffices as it applies to both robots and vertebrates. When the analysis continues on to consider muscle mechanics and its neural control, I will prefer to use the term musculotendon. 


**Forum and commentary:**

_____________________

*Coming soon!*


**Exercises:**

__________

*Coming soon!*



**Additional references and suggested reading:**

____________________________________________

*Coming soon!*



**References in book:**

___________________

1. F.J. Valero-Cuevas, H. Hoffmann, M.U. Kurse, J.J. Kutch, E.A. Theodorou, Computational models for neuromuscular function. IEEE Rev. Biomed. Eng. 2, 110–135 (2009) 
2. F.E. Zajac, Muscle and tendon: properties, models, scaling, and application to biomechanics and motor control. Crit. Rev. Biomed. Eng. 17(4), 359–411 (1989) 
3. F.E.Zajac,Howmusculotendonarchitectureandjointgeometryaffectthecapacityofmuscles to move and exert force on objects: a review with application to arm and forearm tendon transfer design. J. Am. Hand Surg. 17(5), 799–804 (1992) 
4. K.N. An, Y. Ueba, E.Y. Chao, W.P. Cooney, R.L. Linscheid, Tendon excursion and moment arm of index finger muscles. J. Biomech. 16(6), 419–425 (1983) 
5. M.U. Kurse, H. Lipson, F.J. Valero-Cuevas, Extrapolatable analytical functions for tendon excursions and moment arms from sparse datasets. IEEE Trans. Biomed. Eng. 59(6), 1572– 1582 (2012) 
6. F.J. Valero-Cuevas, A mathematical approach to the mechanical capabilities of limbs and fingers. Adv. Exp. Med. Biol. 629, 619–633 (2009) 
7. N.A.Bernstein,TheCo-ordinationandRegulationofMovements(PergamonPress,NewYork, 1967) 
8. F.J.Valero-Cuevas,B.A.Cohn,H.F.Yngvason,E.L.Lawrence,Exploringthehigh-dimensional structure of muscle redundancy via subject-specific and generic musculoskeletal models. J. Biomech. 48(11), 2887–2896 (2015) 
9. V.Chvatal,LinearProgramming(W.H.FreemanandCompany,NewYork,1983) 
10. G.Strang,IntroductiontoLinearAlgebra(WellesleyCambridgePress,Wellesley,2003) 
11. P.E.Gill,W.Murray,M.H.Wright,PracticalOptimization(AcademicPress,NewYork,1981) 
12. J.M. Inouye, J.J. Kutch, F.J. Valero-Cuevas, A novel synthesis of computational approaches 
enables optimization of grasp quality of tendon-driven hands. IEEE Trans. Robot. 28(4), 958– 
966 (2012) 
13. R.A.Henson,H.Urich,Schumann’shandinjury.Br.Med.J.1(6117),900(1978) 
14. M.H.Schieber,M.Santello,Handfunction:peripheralandcentralconstraintsonperformance. 
J. Appl. Physiol. 96(6), 2293–2300 (2004) 
15. C.S.Sherrington,Reflexinhibitionasafactorintheco-ordinationofmovementsandpostures. 
Exp. Physiol. 6(3), 251–310 (1913) 
16. J.J. Kutch, F.J. Valero-Cuevas, Challenges and new approaches to proving the existence of 
muscle synergies of neural origin. PLoS Comput. Biol. 8(5), e1002434 (2012) 


**Code:**

_____

simple\_excursion\_example.m: <a href="/Code/simple_excursion_example.m" download> Download </a>
<script src="https://gist.github.com/aboling/5e4518ae75d9101b8af8345c48a6ba10.js"></script>

simple\_excursion\_example.py: <a href="/Code/simple_excursion_example.py" download> Download </a>
<script src="https://gist.github.com/aboling/7a83c1139f12d2580d8bd84b89058e2d.js"></script>

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<div class="container">
  <ul class="pagination">
    <li><a href="//valerolab.org/book_chapters/ch1.html">Ch. 1</a></li>
    <li><a href="//valerolab.org/book_chapters/ch2.html">Ch. 2</a></li>
    <li><a href="//valerolab.org/book_chapters/ch3.html">Ch. 3</a></li>
    <li class="active"><a href="//valerolab.org/book_chapters/ch4.html">Ch. 4</a></li>
    <li><a href="//valerolab.org/book_chapters/ch5.html">Ch. 5</a></li>
    <li><a href="//valerolab.org/book_chapters/ch6.html">Ch. 6</a></li>
    <li><a href="//valerolab.org/book_chapters/ch7.html">Ch. 7</a></li>
    <li><a href="//valerolab.org/book_chapters/ch8.html">Ch. 8</a></li>
    <li><a href="//valerolab.org/book_chapters/ch9.html">Ch. 9</a></li>
    <li><a href="//valerolab.org/book_chapters/ch10.html">Ch. 10</a></li>
  </ul>
  
</div>



© Francisco Valero-Cuevas 2015
