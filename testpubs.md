---
layout: page
title: Test Publications
permalink: /testpubs/
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

<table>
    <tr>
        <th>Citation</th>
        <th>PDF</th>
        <th>Year</th>
    </tr>

      <tr title="Vertebrate systems operate limbs with many more muscles than degrees of freedom, which creates redundancies for isometric force production. Optimization is usually proposed as the means by which the nervous system solves such underdetermined problem. However, the learning and execution problem can also be approached from the geometric perspective of heuristic or systematic exploration of high-dimensional spaces, and exploitation of feasible regions found and remembered. We apply such approach to assess the learnability of the input-tension to output fingertip force mapping for the seven tendons of a human cadaver index finger. We applied five thousand different 7-dimensional tension vectors, while simultaneously recording the resulting isometric fingertip force outputs. We analyzed the relationship between the input and output in both the forward and inverse directions using. a linear regression model, an Artificial Neural Network, and a data-driven Nearest-Neighbor lookup table. We find that forward models perform more accurately than inverse models and that the Nearest-Neighbor approach has a notable fit error at the edges of the input space. These results open a new front for a thorough understanding of how the actual physics of an anatomical system (i.e., the plant the brain must contend with) fundamentally affects learning, memory, and performance of motor function in health, disease, and in an evolutionary context. Figure 1: A parallel coordinate plot of 5000 muscle tension patterns implemented on a human cadaver finger highlights how sparsely the edges of the input space are explored with uniform sampling.">
        <td>Cohn BA, Marjaninejad A, Valero-Cuevas FJ<br>
            <b>"Evaluating the learnability-dimensionality relationship in a tendon-driven finger"</b> <br>
            Proceedings of the 48th Annual Meeting of the Society for Neuroscience, San Diego, CA, USA, Nov 2018</td>
        <td><a href="../Abstracts/cohn_sfn_2018.pdf">Link</a></td>
        <td>2018</td>
      </tr>


      <tr title="Deciding how to move the hand along a given path to produce activities for daily living (ADLs) involves multiple factors such as limb kinetics, choice of muscle activation patterns, online error corrections, robustness to perturbations, accounting for length/velocity muscle mechanics and time-sensitive reflex modulation. In Hagen & Valero-Cuevas (2017) we show how the joint rotations associated with different paths induce different musculotendon (MT) velocities. While different paths will naturally produce different MT velocities, we found that similar paths can exhibit different MT velocity profiles. This matters at the level of individual muscles because differences in MT velocities will require unique muscle activation strategies to compensate for force-length/force-velocity properties and modulation of their spinal reflex mechanisms. Importantly, these differences in MT velocities within and across paths establish the neuromechanical landscape that determines the robustness of muscle coordination patterns and reflex modulation strategies during ADLs.Here we study how initial variability in the direction of a hand path affects the subsequent time histories of MT velocities. As in our prior work, we used an 18 muscle, 2 joint planar arm model to produce 100 random reaching paths for 6 different pairs of points on a tabletop (3 pairs shared the starting position, 3 pairs shared the ending location). Each valid, smooth reaching path was generated (and its MT velocities found) using a pseudo-random clamped cubic spline, parameterized to follow a bell-shaped tangential velocity curve, simulating reaching movements of 35 cm in length with initial errors compatible with those seen in reaching studies in humans.We find that uniform initial error (i.e., variability) across paths induces non-uniform distributions of MT velocities. That is, although the induced MT velocities follow a similar profile for each reaching movement, their distributions/deviations change across them. This implies that some reaching paths may be more or less forgiving to initial errors in muscle coordination or reflex modulation. This has important consequences to the study of healthy movement, as well as the rehabilitation of movement for ADLs in neurological conditions and stroke.">
        <td>Hagen DA, Laine CM, Chakravarthi Raja S, Valero-Cuevas FJ<br>
            <b>"Small errors in movement paths can induce dramatic changes in musculotendon velocities"</b> <br>
            Proceedings of the 48th Annual Meeting of the Society for Neuroscience, San Diego, CA, USA, Nov 2018</td>
        <td><a href="../Abstracts/hagen_sfn_2018.pdf">Link</a></td>
        <td>2018</td>
      </tr>

      <tr title="Involuntary force variability is an inherent property of motor behavior. When exacerbated, it is a key contributor to performance errors and a feature of several neurological conditions. Some propose that involuntary force variability arises primarily through the conversion of motoneuron firing patterns into muscle force, i.e. “motor noise.” This mechanism has been tested using a model of recruitment and rate coding developed by Fuglevand et al. (1993). However, this model has several drawbacks that limit its ability to simulate force variability. First, it does not explicitly model the fusion of force twitches with increases in firing rate and concomitant saturation of calcium binding to troponin. Second, the model lacks a series elastic element (i.e., tendon), which damps out the effects of fluctuations of motoneurone firing by changing its length and, thereby, the velocity of the muscle fibers in an externally isometric system. We addressed these limitations by combining some elements of the Fuglevand model with physiological and mechanical features from a model by Song et al. (2008). This new model has improved predictions of force and force variability. Upon close inspection, we show the amplitude and spectral features of force variability are significantly influenced by the viscoelastic properties of musculotendons. This model of motor units produces a lower amplitude of force variability than previous models. Also, spectral features of this new model resemble more closely what has been observed experimentally. These results question current thinking attributing the majority of involuntary force variability to peripheral motor noise, and highlight the importance of closed-loop behavior including afferent feedback and error corrections.">
        <td>Nagamori A, Laine CM, Loeb GE, Valero-Cuevas FJ<br>
            <b>"Can Motor Noise Account for Force Variability?"</b> <br>
            Proceedings of the 48th Annual Meeting of the Society for Neuroscience, San Diego, CA, USA, Nov 2018</td>
        <td><a href="../Abstracts/Akira_Nagamori_SfN_2018_Abstract.pdf">Link</a></td>
        <td>2018</td>
      </tr>


      <tr title="In Niu, et al. (2017) we implemented a realtime Field-Programmable Gate Array  (FPGA)-based simulation of neuromorphic models of monosynaptic stretch reflex circuitry of an agonist-antagonist muscle-pair. We then characterized the system in Jalaleddini, et al. (2017) by coupling the simulation to the flexor digitorum profundus and the extensor carpi radialis longus tendons of the MCP joint of a cadaveric hand preparation to show that such systems can indeed evoke human-like stretch reflexes as in the work of Edin and Vallbo (1990). We now present improvements to that system such as including Golgi tendon organs, Renshaw cells, and polysynaptic interneuronal pathways to form a system akin to a simplified spinal-like regulator as in Raphael et al. (2010). Nonlinear adaptive controls and simple neural networks allow us tune the descending commands (pulse trains) to both fusimotor and alpha motoneuron pools. We use such time-based running of descending commands to demonstrate the ability to produce “voluntary” movement. We find that realistic models of muscle mechanics, force-velocity properties in particular, are critical to produce stable movements. By selectively adding/removing components and interconnections, we are also able to show the sufficiency of the same for enabling voluntary movement. Future extensions will include homonymous and heteronymous sensorimotor pathways to control more muscles and produce motor function in cadaveric human fingers.">
        <td>Chakravarthi Raja S, Valero-Cuevas FJ.<br>
            <b>"An integrative neuromorphic approach to modeling of voluntary motor function."</b> <br>
            Proceedings of the 48th Annual Meeting of the Society for Neuroscience, San Diego, CA, USA, Nov 2018</td>
        <td><a href="../Abstracts/2018_SCRaja_SfNAbstract.pdf">Link</a></td>
        <td>2018</td>
      </tr>


      <tr>
        <td>Nagamori A, Laine CM, Valero-Cuevas FJ<br>
            <b>"A computational model of afferented muscles reproduces cardinal features of force variability"</b> <br>
            Proceedings of the 28th Annual Meeting of the Society for the Neural Control of Movement, Santa Fe, New Mexico, USA, May 2018</td>
        <td><a href="../Abstracts/AN_NCM_Abstract_2018.pdf">Link</a></td>
        <td>2018</td>
      </tr>


      <tr>
        <td>Cohn BA, Jalaleddini K, Valero-Cuevas FJ <br>
            <b>"Neuromechanical implications of postural changes to motor learning and performance"</b> <br>
            Proceedings of the 41st Annual Meeting of the American Society of Biomechanics, Boulder, CO. Aug 8-11, 2017.</td>
        <td><a href="../Papers/cohn_jalaleddini_valerocuevas_asb_2017.pdf">Link</a></td>
        <td>2017</td>
      </tr>


      <tr>
        <td>Jalaleddini K, Nagamori A, Laine CM, Golkar MA, Kearney RE, Valero-Cuevas FJ<br>
            <b>"Evidence That Tuning of Muscle Spindles Can Be Decoupled from Muscle Activation"</b> <br>
            Proceedings of the 41st Annual Meeting of the American Society of Biomechanics, Boulder, CO. Aug 8-11, 2017.</td>
        <td><a href="../Papers/ASB2017_Poster_Kian.pdf">Link</a></td>
        <td>2017</td>
      </tr>


      <tr>
        <td> Marjaninejad A, Taherian B, Jalaleddini K, and Valero-Cuevas FJ <br>
            <b>"Simple and Two-Element Hill-Type Muscle Models Cannot Replicate Realistic Muscle Stiffness"</b> <br>
            Proceedings of the 41st Annual Meeting of the American Society of Biomechanics, Boulder, CO. Aug 8-11, 2017.</td>
        <td><a href="../Papers/Ko2016Dynamic.pdf">Link</a></td>
        <td>2017</td>
      </tr>

      <tr>
        <td>Nagamori A, Laine CM, Jalaleddini K, Valero-Cuevas FJ<br>
            <b>"Interactions between Tendon Stiffness and Spindle Afferent Feedback Determine the Magnitude of Involuntary Force Variability"</b> <br>
            Proceedings of the 41st Annual Meeting of the American Society of Biomechanics, Boulder, CO. Aug 8-11, 2017.</td>
        <td><a href="../Papers/ASB_2017_nagamori.pdf">Link</a></td>
        <td>2017</td>
      </tr>

      <tr>
        <td>Laine CM, Valero-Cuevas FJ<br>
            <b>"Specific Manual Tasks Transform EMG into a Probe for Neural Dysfunction in Parkinson’s Disease"</b> <br>
            Proceedings of the 41st Annual Meeting of the American Society of Biomechanics, Boulder, CO. Aug 8-11, 2017.</td>
        <td><a href="../Papers/CML_FJVC_ASB_2017.pdf">Link</a></td>
        <td>2017</td>
      </tr>

        <tr>
          <td>Ko N, Laine CM, Fisher BE, Valero-Cuevas FJ. <br>
              <b>"Dynamic fingertip force variability in individuals with Parkinsons disease."</b> <br>
              Hand Rehabilitation Section, American Physical Therapy Association Combined Sections Meeting, Anaheim, CA, Feb 17-20, 2016.</td>
          <td><a href="../Papers/Ko2016Dynamic.pdf">Link</a></td>
          <td>2016</td>
        </tr>

        <tr>
          <td>Lawrence EL, Nagamori A, Valero-Cuevas FJ, Finley JM.<br>
              <b>"Prolonged immobilization and unloading leads to profound and long-lasting changes in spinal excitability."</b> <br>
              Proceedings of the 44th Annual Meeting of the Society for Neuroscience, Washington DC, November 15-19, 2014.</td>
          <td></td>
          <td>2014</td>
        </tr>

        <tr>
          <td>Lawrence EL, Lyle MA, Werner I, Krenn O, Lorenzi D, Kernbeiss S, Gondolatsch B, Frontull V, Zarfl M, Posch M, Valero-Cuevas FJ. <br>
              <b>"Participation in elite sports improves neuromuscular control as detected by the Lower Extremity Strength-Dexterity Test."</b> <br>
              Proceedings of the 43rd Annual Meeting of the Society for Neuroscience, San Diego, CA, November 9-13, 2013.</td>
          <td></td>
          <td>2013</td>
        </tr>

        <tr>
          <td>Ko N*, Lawrence EL*, Dayanidhi S*, Hu W, DiConti A, Lerner J, Winstein CW, Requejo P, Fisher B, Valero-Cuevas FJ. <br>
              <b>"The Strength-Dexterity test can detect differences in dynamic control of fingertip forces between individuals with Parkinson's disease and non-disabled older adults."</b> <br>
              Proceedings of the 43rd Annual Meeting of the Society for Neuroscience, San Diego, CA, November 9-13, 2013. *denotes equal contribution</td>
          <td></td>
          <td>2013</td>
        </tr>

        <tr>
          <td>Rocamora JM, Niu CM, Buchli J, Sanger TD, Valero-Cuevas FJ. <br>
              <b>"Physiologically-based control of a robotic tendon-driven system."</b> <br>
              Proceedings of the 43rd Annual Meeting of the Society for Neuroscience, San Diego, CA, November 9-13, 2013.</td>
          <td></td>
          <td>2013</td>
        </tr>

        <tr>
          <td>Babikian S, Kanso E, Valero-Cuevas FJ. <br>
              <b>"Pre-tensioning of musculotendons is necessary to achieve finger postures and slow finger motions."</b> <br>
              Proceedings of the 43rd annual meeting of the Society for Neuroscience, San Diego, CA, November 9-13, 2013.</td>
          <td></td>
          <td>2013</td>
        </tr>

        <tr>
          <td>Reyes A, Lawrence EL, Babikian S, Liu CY, Heck CN, Valero-Cuevas FJ. <br>
              <b>"Spectral activity of cortical activity during manipulation of unstable objects revels task-dependent spatiotemporal features."</b> <br>
              Proceedings of the 43rd Annual Meeting of the Society for Neuroscience, San Diego, CA, November 9-13, 2013.</td>
          <td></td>
          <td>2013</td>
        </tr>

        <tr>
          <td>Kurse MU, Schmidt M, Lipson H, Valero-Cuevas FJ. <br>
              <b>Extracting mathematical models defining index finger kinematics using symbolic regression.</b> <br>
              Proceedings of the 14th Annual Fred S. Grodins Graduate Research Symposium, Los Angeles, CA, April 10th, 2010. </td>
          <td><a href="https://usc-bbdl.github.io/Papers/Kurse2010mathematical.pdf">Link</a></td>
          <td>2010</td>
        </tr>

        <tr>
          <td>Kurse MU, Valero-Cuevas FJ., Lipson H. <br>
              <b>Estimating the Topology of the Extensor Mechanism of the Human Finger.</b> <br>
              Proceedings of the 12th Annual Fred S. Grodins Graduate Research Symposium, Los Angeles, CA, April 5th, 2010. </td>
          <td></td>
          <td>2010</td>
        </tr>

        <tr>
          <td>R&aacute;cz, K, Valero-Cuevas FJ.<br>
              <b>"Motion and force are not controlled independently in multi-finger manipulation tasks."</b> <br>
              40th Annual Meeting of the Society for Neuroscience, San Diego, CA, 2010.</td>
          <td></td>
          <td>2010</td>
        </tr>

        <tr>
          <td>Kutch JJ, Kurse MU, Valero-Cuevas FJ <br>
              <b>"Muscle redundancy does not imply robustness to muscle dysfunction"</b> <br>
              40th Annual Meeting of the Society for Neuroscience, San Diego CA, November 2010.</td>
          <td><a href="https://usc-bbdl.github.io/Papers/Kutch2010Muscle.pdf">Link</a></td>
          <td>2010</td>
        </tr>

        <tr>
          <td>Kutch JJ, Valero-Cuevas FJ <br>
              <b>"Obtaining complete solution sets for neuromuscular models"</b> <br>
              ASME 2010 Summer Bioengineering Conference, Naples, FL, June 2010.</td>
          <td></td>
          <td>2010</td>
        </tr>

        <tr>
          <td>Kutch JJ, Kurse MU, Hoffmann H, Kuo AD, Valero-Cuevas FJ. <br>
              <b>"Muscle synergies may be artifacts of biomechanics rather than neural constraints, and are not necessary to simplify control"</b> <br>
              39th Annual Meeting of the Society for Neuroscience, Chicago IL, October 2009.</td>
          <td></td>
          <td>2009</td>
        </tr>

        <tr>
          <td>R&aacute;cz, K, Inouye J, Valero-Cuevas FJ. <br>
              <b>"The spatio-temporal structure of force variability in static grasp suggests a continually active neural controller."</b> <br>
              Summer Bioengineering Conference of the American Society of Mechanical Engineers, Naples, FL, 2010.</td>
          <td><a href="https://usc-bbdl.github.io/Papers/Kornelius2010spatio.pdf">Link</a></td>
          <td>2010</td>
        </tr>

        <tr>
          <td>Kuxhaus LC, Valero-Cuevas FJ, and Roach SS. <br>
              <b>Effect of simulated low ulnar nerve palsy on the 3D force production capabilities of the thumb.</b> <br>
              Upstate Medical University Alumni Day, Syracuse University, Syracuse, NY, 2003.</td>
          <td></td>
          <td>2003</td>
        </tr>

        <tr>
          <td>Santos VJ and Valero-Cuevas FJ. <br>
              <b>Stochastic analysis of anatomical data suggests three characteristic types of thumb kinematics. </b> <br>
              Proceedings of the American Society of Mechanical Engineers Summer Bioengineering Conference, Key Biscayne, FL. 2003.</td>
          <td><a href="https://usc-bbdl.github.io/Papers/Santos2003Stochastic.PDF">Link</a></td>
          <td>2003</td>
        </tr>

        <tr>
          <td>Venkadesan M, Valero-Cuevas FJ, Guckenheimer JM. <br>
              <b>The dynamic sensorimotor regulation of fingertip force vectors is independent of hand strength.</b> <br>
              33th Annual Meeting of the Society for Neuroscience. New Orleans, LA, 2003.</td>
          <td><a href="https://usc-bbdl.github.io/Papers/Venkadesan2003dynamic.pdf">Link</a></td>
          <td>2003</td>
        </tr>

        <tr>
          <td>Valero-Cuevas FJ, Venkadesan, M, Talati, A Hirsch J. <br>
              <b>How networks of cortical activity adapt in response to changes in the type and quality of sensory input during dynamic precision pinch.</b> <br>
              32th Annual Meeting of the Society for Neuroscience. Orlando, FL, 2002.</td>
          <td></td>
          <td>2002</td>
        </tr>

        <tr>
          <td>Valero-Cuevas FJ, Burgar CG, Johanson ME, Zajac FE. <br>
              <b>Scaling of muscle activation patterns during generation of isometric fingertip forces. </b> <br>
              28th Annual Meeting of the Society for Neuroscience. Los Angeles, CA, 1998.</td>
          <td></td>
          <td>1998</td>
        </tr>

        <tr>
          <td>Valero-Cuevas FJ, Burgar C, Zajac FE, Hentz VR, McGill KC, An KN. <br>
              <b>Muscle coordination during maximal index-finger ad-abduction forces. </b> <br>
              Abstracts V. I, 26th Annual Meeting of the Society for Neuroscience, Washington, DC., 1996.</td>
          <td></td>
          <td>1996</td>
        </tr>


</table>
 
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
<!-- scroll to top button -->
 
</body>
