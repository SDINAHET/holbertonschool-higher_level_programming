<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="google" content="notranslate">
    <title>Project: Python - Data Structures: Lists, Tuples | Holberton Rennes, France Intranet</title>
      <link rel="stylesheet" href="https://use.typekit.net/xgz4ilr.css">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css">
      <link rel="stylesheet" media="all" href="/assets/application-82f828a36761ddaf87c87d57bfdf65ea423ccdbd071f956e4ad4b74a2662418c.css" />
      <script src="https://www.gstatic.com/charts/loader.js"></script>
      <meta name="action-cable-url" content="/cable" />
      <script src="/assets/application-08d13bb8d36999e13c0e8ca3172174cb5977d17ff1b0efa16aab65be73c6fa77.js"></script>
      <link rel="shortcut icon" type="image/x-icon" href="/favicon.ico" />
      <meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="fvohPmJLEbowB3N_HXpH1PHPl_BYjdk7I6AHRBqswV5Bau0Q8SAbbHXJJipKZ7pDncIqcOfmKsO5yF7JErumGQ" />
      <link rel="apple-touch-icon" href="/apple-touch-icon.png">
      <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
      <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
      <![endif]-->
      <!-- Store user timezone -->
      <script>
        Cookies.set('timezone', (new Date()).getTimezoneOffset() / -60.0);
      </script>
      <!-- intro.js for interactive onboarding -->
        <script src="https://unpkg.com/intro.js/minified/intro.min.js"></script>
        <link rel="stylesheet" media="screen" href="https://unpkg.com/intro.js/minified/introjs.min.css" />
      <!-- React -->
      <script src="/packs/js/application-1669a610fadcabe33c99.js"></script>
      <link rel="stylesheet" media="screen" href="/packs/css/application-87456da7.css" />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"
    />
  </head>
  <body class="
    signed_in
    env_production

    "
    translate="no"
    class="notranslate"
    data-theme-suffix=""
    data-checker-special-theme="">
      <input type="hidden" id="hbtn-slack-url" value="https://holberton-school-org.slack.com">
      <nav class="navbar navbar-default navbar-fixed-top topbar visible-xs">
  <div class="navbar-header">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-mobile" aria-expanded="false">
      <span class="sr-only">Toggle navigation</span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
    </button>

    <a class="navbar-brand" href="/">
      <div class="logo"></div>
</a>  </div>

  <div class="collapse navbar-collapse navigation" id="navbar-mobile">
    <ul class="nav navbar-nav">

    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Help"><a target="_blank" href="https://students-support.hbtn.io/hc"><div class="icon "><i aria-hidden="true" class="fa fa-info-circle "></i></div><div class="visible-xs">Help</div></a></li>



    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-current-projects-item" title="Projects"><a href="/projects/current"><div class="icon "><i aria-hidden="true" class="fa fa-code-fork "></i></div><div class="visible-xs">Projects</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="My reports"><a href="/users/my_reports"><div class="icon "><i aria-hidden="true" class="fa fa-sticky-note-o "></i></div><div class="visible-xs">My reports</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="QA Reviews I can make"><a href="/corrections/to_review"><div class="icon "><i aria-hidden="true" class="fa fa-check "></i></div><div class="visible-xs">QA Reviews I can make</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Mock interviews"><a href="/dashboards/my_current_reefineries"><div class="icon "><i aria-hidden="true" class="fa fa-commenting-o "></i></div><div class="visible-xs">Mock interviews</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Evaluation quizzes"><a href="/dashboards/my_current_evaluation_quizzes"><div class="icon "><i aria-hidden="true" class="fa fa-question "></i></div><div class="visible-xs">Evaluation quizzes</div></a></li>

    <hr title="My resources">


    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-concepts-item" title="Concepts"><a href="/concepts"><div class="icon "><i aria-hidden="true" class="fa fa-file-text "></i></div><div class="visible-xs">Concepts</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Servers"><a href="/servers"><div class="icon "><i aria-hidden="true" class="fa fa-server "></i></div><div class="visible-xs">Servers</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-containers" title="Sandboxes"><a href="/user_sandboxes"><div class="icon "><i aria-hidden="true" class="fa fa-terminal "></i></div><div class="visible-xs">Sandboxes</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Tools"><a href="/dashboards/my_tools"><div class="icon "><i aria-hidden="true" class="fa fa-wrench "></i></div><div class="visible-xs">Tools</div></a></li>

      <hr title="My campus">


      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Peers"><a href="/users/peers"><div class="icon "><i aria-hidden="true" class="fa fa-users "></i></div><div class="visible-xs">Peers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Captain&#39;s Logs"><a href="/dashboards/my_captain_log"><div class="icon "><i aria-hidden="true" class="fa fa-book "></i></div><div class="visible-xs">Captain&#39;s Logs</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Officers"><a href="/dashboards/my_officers"><div class="icon "><i aria-hidden="true" class="fa fa-building "></i></div><div class="visible-xs">Officers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Speakers of the Day"><a href="/dashboards/my_speakers_of_the_day"><div class="icon "><i aria-hidden="true" class="fa fa-microphone "></i></div><div class="visible-xs">Speakers of the Day</div></a></li>


<hr class="visible-xs">

<li>
    <div
      data-container="body"
      data-placement="right"
      data-toggle="tooltip"
      title="Slack">
      <a target="_blank" href="https://holberton-school-org.slack.com">
        <div class="image slack">
          <div class="inner"></div>
        </div>
        <div class="visible-xs">Slack</div>
</a>    </div>

    <div
      data-container="body"
      data-placement="right"
      data-toggle="modal"
      data-target="#search-modal"
      title="Search">
      <a href="#">
          <div class="icon">
            <i aria-hidden="true" class="fa fa-search "></i>
          </div>
        <div class="visible-xs">Search</div>
</a>    </div>

  <div
    data-container="body"
    data-placement="right"
    data-toggle="tooltip"
    title="My Profile">
    <a href="/users/my_profile">
        <div class="image ">
          <div class="inner" style="background-image: url('https://s3.eu-west-3.amazonaws.com/hbtn.intranet/users/photos/000/009/546/thumb/Capture_d%E2%80%99%C3%A9cran_2024-06-03_111954.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240909%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20240909T095053Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=c31f520855c6969208d413dbb7171492114677799cb36dd1ee192f7c3165915d')"></div>
        </div>

      <div class="visible-xs">My Profile</div>
</a>  </div>
</li>


    </ul>
  </div>
</nav>

      <div class="hidden-xs navigation sidebar">
  <a class="logo-container" href="/">
    <div class="logo"></div>
</a>
  <ul>

    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Help"><a target="_blank" href="https://students-support.hbtn.io/hc"><div class="icon "><i aria-hidden="true" class="fa fa-info-circle "></i></div><div class="visible-xs">Help</div></a></li>



    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-current-projects-item" title="Projects"><a href="/projects/current"><div class="icon "><i aria-hidden="true" class="fa fa-code-fork "></i></div><div class="visible-xs">Projects</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="My reports"><a href="/users/my_reports"><div class="icon "><i aria-hidden="true" class="fa fa-sticky-note-o "></i></div><div class="visible-xs">My reports</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="QA Reviews I can make"><a href="/corrections/to_review"><div class="icon "><i aria-hidden="true" class="fa fa-check "></i></div><div class="visible-xs">QA Reviews I can make</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Mock interviews"><a href="/dashboards/my_current_reefineries"><div class="icon "><i aria-hidden="true" class="fa fa-commenting-o "></i></div><div class="visible-xs">Mock interviews</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Evaluation quizzes"><a href="/dashboards/my_current_evaluation_quizzes"><div class="icon "><i aria-hidden="true" class="fa fa-question "></i></div><div class="visible-xs">Evaluation quizzes</div></a></li>

    <hr title="My resources">


    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-concepts-item" title="Concepts"><a href="/concepts"><div class="icon "><i aria-hidden="true" class="fa fa-file-text "></i></div><div class="visible-xs">Concepts</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Servers"><a href="/servers"><div class="icon "><i aria-hidden="true" class="fa fa-server "></i></div><div class="visible-xs">Servers</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-containers" title="Sandboxes"><a href="/user_sandboxes"><div class="icon "><i aria-hidden="true" class="fa fa-terminal "></i></div><div class="visible-xs">Sandboxes</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Tools"><a href="/dashboards/my_tools"><div class="icon "><i aria-hidden="true" class="fa fa-wrench "></i></div><div class="visible-xs">Tools</div></a></li>

      <hr title="My campus">


      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Peers"><a href="/users/peers"><div class="icon "><i aria-hidden="true" class="fa fa-users "></i></div><div class="visible-xs">Peers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Captain&#39;s Logs"><a href="/dashboards/my_captain_log"><div class="icon "><i aria-hidden="true" class="fa fa-book "></i></div><div class="visible-xs">Captain&#39;s Logs</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Officers"><a href="/dashboards/my_officers"><div class="icon "><i aria-hidden="true" class="fa fa-building "></i></div><div class="visible-xs">Officers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Speakers of the Day"><a href="/dashboards/my_speakers_of_the_day"><div class="icon "><i aria-hidden="true" class="fa fa-microphone "></i></div><div class="visible-xs">Speakers of the Day</div></a></li>


<hr class="visible-xs">

<li>
    <div
      data-container="body"
      data-placement="right"
      data-toggle="tooltip"
      title="Slack">
      <a target="_blank" href="https://holberton-school-org.slack.com">
        <div class="image slack">
          <div class="inner"></div>
        </div>
        <div class="visible-xs">Slack</div>
</a>    </div>

    <div
      data-container="body"
      data-placement="right"
      data-toggle="modal"
      data-target="#search-modal"
      title="Search">
      <a href="#">
          <div class="icon">
            <i aria-hidden="true" class="fa fa-search "></i>
          </div>
        <div class="visible-xs">Search</div>
</a>    </div>

  <div
    data-container="body"
    data-placement="right"
    data-toggle="tooltip"
    title="My Profile">
    <a href="/users/my_profile">
        <div class="image ">
          <div class="inner" style="background-image: url('https://s3.eu-west-3.amazonaws.com/hbtn.intranet/users/photos/000/009/546/thumb/Capture_d%E2%80%99%C3%A9cran_2024-06-03_111954.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240909%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20240909T095053Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=c31f520855c6969208d413dbb7171492114677799cb36dd1ee192f7c3165915d')"></div>
        </div>

      <div class="visible-xs">My Profile</div>
</a>  </div>
</li>


  </ul>
</div>

    <main>
      <div id="layout-bars">

        <div class="px-5 py-3" id="student-switch-curriculum">
  <div class="dropdown d-flex flex-column gap-1">
    <span class="fs-small text-muted">Curriculum</span>
    <div aria-haspopup="true" aria-expanded="false" class="align-items-center d-flex gap-3" data-toggle="dropdown" id="student-switch-curriculum-dropdown" role="button">
      <div class="d-flex flex-column" style="line-height: 16px">
        <span class="fs-4 fw-600">
            [C#24]
          Foundations v2 - Part 2
        </span>
        <span class="fs-small text-muted">
          Average: <span class="fw-500">100.0%</span>
        </span>
      </div>
      <div class="d-flex flex-column justify-content-center">
        <span style="margin-bottom: -4px">
          <i aria-hidden="true" class="fa fa-angle-up  fa-fw"></i>
        </span>
        <span style="margin-top: -4px">
          <i aria-hidden="true" class="fa fa-angle-down  fa-fw"></i>
        </span>
      </div>
    </div>
    <ul aria-labelledby="student-switch-curriculum-dropdown" class="dropdown-menu fs-5">
        <li>
          <a class="" href="/curriculums/327/observe/37959">
            <div class="align-items-center d-flex py-2">
              <div class="d-flex flex-column" style="line-height: 16px">
                <span class="fs-4 fw-500">
                    [C#24]
                  Foundations v2 - Part 1
                </span>
                <span class="text-muted">
                  Average: <span class="fw-500">97.39%
                          </span>
                </span>
              </div>
            </div>
</a>        </li>
        <li>
          <a class="" href="/curriculums/392/observe/45551">
            <div class="align-items-center d-flex py-2">
              <div class="d-flex flex-column" style="line-height: 16px">
                <span class="fs-4 fw-500">
                    [C#24]
                  HBnB v2
                </span>
                <span class="text-muted">
                  Average: <span class="fw-500">%
                          </span>
                </span>
              </div>
            </div>
</a>        </li>
        <li>
          <a class="" href="/curriculums/394/observe/45832">
            <div class="align-items-center d-flex py-2">
              <div class="d-flex flex-column" style="line-height: 16px">
                <span class="fs-4 fw-500">
                    [C#24]
                  Foundations v2 - Part 2
                </span>
                <span class="text-muted">
                  Average: <span class="fw-500">100.0%
                          </span>
                </span>
              </div>
                <span class="fw-600 text-info" style="margin-left: 42px">
                  <i aria-hidden="true" class="fa fa-check "></i>
                </span>
            </div>
</a>        </li>
    </ul>
  </div>
</div>




      </div>
      <article class="">

<div class="project row">
  <div class="col-xs-12 col-md-10 col-lg-8 contains-images">

      <div class="sm-gap">
    <div data-react-class="projects/ProjectHeader" data-react-props="{&quot;metadata&quot;:{&quot;level&quot;:&quot;Novice&quot;,&quot;author&quot;:&quot;Guillaume&quot;,&quot;weight&quot;:1,&quot;migrated_to_sasheck&quot;:true,&quot;task_level_review_type&quot;:&quot;Your score will be updated as you progress.&quot;,&quot;correction&quot;:{&quot;released&quot;:false,&quot;requires_manual_correction&quot;:false}},&quot;project&quot;:{&quot;completion&quot;:0.0,&quot;id&quot;:2120,&quot;index&quot;:0,&quot;isAccessible&quot;:true,&quot;isOptional&quot;:false,&quot;imagePath&quot;:&quot;/assets/pathway/003_color-0c5b38973bfe29fff8dd86f65a213ea2d2499a7d0d9e4549f440c50dc84c9618.png&quot;,&quot;name&quot;:&quot;Python - Data Structures: Lists, Tuples&quot;,&quot;score&quot;:{&quot;mandatory&quot;:0.0,&quot;optional&quot;:0.0},&quot;tasksCount&quot;:0},&quot;slackLink&quot;:null,&quot;tags&quot;:[],&quot;videoRoomLink&quot;:null}" data-react-cache-id="projects/ProjectHeader-0"></div>
  </div>



    <div id="project_id" style="display: none" data-project-id="2120"></div>







      <div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/UCQlbIrhZJVRfxndAcskkw" title="3.1.3. Lists" target="_blank">3.1.3. Lists</a> </li>
<li><a href="/rltoken/89W42byWTSM4e25VSPKMRg" title="Data structures" target="_blank">Data structures</a> (<em>until <code>5.3. Tuples and Sequences</code> included</em>)</li>
<li><a href="/rltoken/JNLdadDW7IWjwW9dbcEyhg" title="Learn to Program 6 : Lists" target="_blank">Learn to Program 6 : Lists</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/EKmHTirCHjvH-IXbBEzi8g" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What are lists and how to use them</li>
<li>What are the differences and similarities between strings and lists</li>
<li>What are the most common methods of lists and how to use them</li>
<li>How to use lists as stacks and queues</li>
<li>What are list comprehensions and how to use them</li>
<li>What are tuples and how to use them</li>
<li>When to use tuples versus lists</li>
<li>What is a sequence</li>
<li>What is tuple packing</li>
<li>What is sequence unpacking</li>
<li>What is the <code>del</code> statement and how to use it</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

  </div>
</div>




        <div class="panel panel-default" id="project-quiz-questions-title">
    <div class="panel-heading">
      <h3 class="panel-title">
        Quiz questions
      </h3>
    </div>

    <div class="panel-body">

        <div class="alert alert-info">
          <strong>Great!</strong>
          You've completed the quiz successfully! Keep going!
          <span id="quiz_questions_collapse_toggle"></span>
        </div>

      <section class="quiz_questions_show_container">
          <div class="quiz_question_item_container" data-role="quiz_question5464" data-position="1">
            <div class=" clearfix" id="quiz_question-5464">

    <h4 class="quiz_question">

        Question #0
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; a = [1, 2, 3, 4]
&gt;&gt;&gt; a[0]
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5464">
                <li class="">

  <input type="radio" name="5464" id="5464-1501190317075" value="1501190317075" data-quiz-answer-id="1501190317075" data-quiz-question-id="5464" disabled="disabled" checked="checked" />
  <label for="5464-1501190317075"><p>1</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5464" id="5464-1501190320955" value="1501190320955" data-quiz-answer-id="1501190320955" data-quiz-question-id="5464" disabled="disabled" />
  <label for="5464-1501190320955"><p>2</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5464" id="5464-1501190324226" value="1501190324226" data-quiz-answer-id="1501190324226" data-quiz-question-id="5464" disabled="disabled" />
  <label for="5464-1501190324226"><p>[1]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5464" id="5464-1501190329957" value="1501190329957" data-quiz-answer-id="1501190329957" data-quiz-question-id="5464" disabled="disabled" />
  <label for="5464-1501190329957"><p>[1, 2]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5464" id="5464-1501190334047" value="1501190334047" data-quiz-answer-id="1501190334047" data-quiz-question-id="5464" disabled="disabled" />
  <label for="5464-1501190334047"><p>[1, 2, 3, 4]</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5465" data-position="2">
            <div class=" clearfix" id="quiz_question-5465">

    <h4 class="quiz_question">

        Question #1
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; a = [1, 2, 3, 4]
&gt;&gt;&gt; a[-1]
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5465">
                <li class="">

  <input type="radio" name="5465" id="5465-1501190347797" value="1501190347797" data-quiz-answer-id="1501190347797" data-quiz-question-id="5465" disabled="disabled" />
  <label for="5465-1501190347797"><p>-1</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5465" id="5465-1501190352432" value="1501190352432" data-quiz-answer-id="1501190352432" data-quiz-question-id="5465" disabled="disabled" />
  <label for="5465-1501190352432"><p>2</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5465" id="5465-1501190358535" value="1501190358535" data-quiz-answer-id="1501190358535" data-quiz-question-id="5465" disabled="disabled" checked="checked" />
  <label for="5465-1501190358535"><p>4</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5465" id="5465-1501190372856" value="1501190372856" data-quiz-answer-id="1501190372856" data-quiz-question-id="5465" disabled="disabled" />
  <label for="5465-1501190372856"><p>[4, 3, 2, 1]</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5466" data-position="3">
            <div class=" clearfix" id="quiz_question-5466">

    <h4 class="quiz_question">

        Question #2
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; a = [1, 2, 3, 4]
&gt;&gt;&gt; a[-3]
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5466">
                <li class="">

  <input type="radio" name="5466" id="5466-1501190387252" value="1501190387252" data-quiz-answer-id="1501190387252" data-quiz-question-id="5466" disabled="disabled" />
  <label for="5466-1501190387252"><p>-3</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5466" id="5466-1501190394041" value="1501190394041" data-quiz-answer-id="1501190394041" data-quiz-question-id="5466" disabled="disabled" />
  <label for="5466-1501190394041"><p>[4, 3]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5466" id="5466-1501190399482" value="1501190399482" data-quiz-answer-id="1501190399482" data-quiz-question-id="5466" disabled="disabled" checked="checked" />
  <label for="5466-1501190399482"><p>2</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5467" data-position="4">
            <div class=" clearfix" id="quiz_question-5467">

    <h4 class="quiz_question">

        Question #3
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; a = [1, 2, 3, 4]
&gt;&gt;&gt; len(a)
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5467">
                <li class="">

  <input type="radio" name="5467" id="5467-1501190411285" value="1501190411285" data-quiz-answer-id="1501190411285" data-quiz-question-id="5467" disabled="disabled" />
  <label for="5467-1501190411285"><p>2</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5467" id="5467-1501190418825" value="1501190418825" data-quiz-answer-id="1501190418825" data-quiz-question-id="5467" disabled="disabled" checked="checked" />
  <label for="5467-1501190418825"><p>4</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5467" id="5467-1501190424235" value="1501190424235" data-quiz-answer-id="1501190424235" data-quiz-question-id="5467" disabled="disabled" />
  <label for="5467-1501190424235"><p>6</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5467" id="5467-1501190426605" value="1501190426605" data-quiz-answer-id="1501190426605" data-quiz-question-id="5467" disabled="disabled" />
  <label for="5467-1501190426605"><p>8</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5468" data-position="5">
            <div class=" clearfix" id="quiz_question-5468">

    <h4 class="quiz_question">

        Question #4
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; a = [1, 2, 3, 4]
&gt;&gt;&gt; a.append(5)
&gt;&gt;&gt; len(a)
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5468">
                <li class="">

  <input type="radio" name="5468" id="5468-1501190430881" value="1501190430881" data-quiz-answer-id="1501190430881" data-quiz-question-id="5468" disabled="disabled" />
  <label for="5468-1501190430881"><p>2</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5468" id="5468-1501190433575" value="1501190433575" data-quiz-answer-id="1501190433575" data-quiz-question-id="5468" disabled="disabled" checked="checked" />
  <label for="5468-1501190433575"><p>5</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5468" id="5468-1501190435865" value="1501190435865" data-quiz-answer-id="1501190435865" data-quiz-question-id="5468" disabled="disabled" />
  <label for="5468-1501190435865"><p>6</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5469" data-position="6">
            <div class=" clearfix" id="quiz_question-5469">

    <h4 class="quiz_question">

        Question #5
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; a = [1, 2, 3, 4]
&gt;&gt;&gt; a[1:3]
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5469">
                <li class="">

  <input type="radio" name="5469" id="5469-1501190452514" value="1501190452514" data-quiz-answer-id="1501190452514" data-quiz-question-id="5469" disabled="disabled" />
  <label for="5469-1501190452514"><p>[1, 2, 3]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5469" id="5469-1501190457702" value="1501190457702" data-quiz-answer-id="1501190457702" data-quiz-question-id="5469" disabled="disabled" />
  <label for="5469-1501190457702"><p>[1, 2]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5469" id="5469-1501190460818" value="1501190460818" data-quiz-answer-id="1501190460818" data-quiz-question-id="5469" disabled="disabled" checked="checked" />
  <label for="5469-1501190460818"><p>[2, 3]</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5470" data-position="7">
            <div class=" clearfix" id="quiz_question-5470">

    <h4 class="quiz_question">

        Question #6
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; a = [1, 2, 3, 4]
&gt;&gt;&gt; a[2] = 10
&gt;&gt;&gt; a
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5470">
                <li class="">

  <input type="radio" name="5470" id="5470-1501190471050" value="1501190471050" data-quiz-answer-id="1501190471050" data-quiz-question-id="5470" disabled="disabled" />
  <label for="5470-1501190471050"><p>[1, 2, 3, 4]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5470" id="5470-1501190480325" value="1501190480325" data-quiz-answer-id="1501190480325" data-quiz-question-id="5470" disabled="disabled" />
  <label for="5470-1501190480325"><p>[1, 10, 3, 4]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5470" id="5470-1501190500395" value="1501190500395" data-quiz-answer-id="1501190500395" data-quiz-question-id="5470" disabled="disabled" checked="checked" />
  <label for="5470-1501190500395"><p>[1, 2, 10, 4]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5470" id="5470-1501190513098" value="1501190513098" data-quiz-answer-id="1501190513098" data-quiz-question-id="5470" disabled="disabled" />
  <label for="5470-1501190513098"><p>[1, 2, 10, 10]</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5471" data-position="8">
            <div class=" clearfix" id="quiz_question-5471">

    <h4 class="quiz_question">

        Question #7
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; a = [1, 2, 3, 4]
&gt;&gt;&gt; b = a
&gt;&gt;&gt; b
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5471">
                <li class="">

  <input type="radio" name="5471" id="5471-1501190520654" value="1501190520654" data-quiz-answer-id="1501190520654" data-quiz-question-id="5471" disabled="disabled" checked="checked" />
  <label for="5471-1501190520654"><p>[1, 2, 3, 4]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5471" id="5471-1501190551898" value="1501190551898" data-quiz-answer-id="1501190551898" data-quiz-question-id="5471" disabled="disabled" />
  <label for="5471-1501190551898"><p>[1]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5471" id="5471-1501190554846" value="1501190554846" data-quiz-answer-id="1501190554846" data-quiz-question-id="5471" disabled="disabled" />
  <label for="5471-1501190554846"><p>1</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5471" id="5471-1501190556587" value="1501190556587" data-quiz-answer-id="1501190556587" data-quiz-question-id="5471" disabled="disabled" />
  <label for="5471-1501190556587"><p>a</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5472" data-position="9">
            <div class=" clearfix" id="quiz_question-5472">

    <h4 class="quiz_question">

        Question #8
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; a = [1, 2, 3, 4]
&gt;&gt;&gt; b = a
&gt;&gt;&gt; a[2] = 10
&gt;&gt;&gt; a
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5472">
                <li class="">

  <input type="radio" name="5472" id="5472-1501190563775" value="1501190563775" data-quiz-answer-id="1501190563775" data-quiz-question-id="5472" disabled="disabled" />
  <label for="5472-1501190563775"><p>[1]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5472" id="5472-1501190572782" value="1501190572782" data-quiz-answer-id="1501190572782" data-quiz-question-id="5472" disabled="disabled" checked="checked" />
  <label for="5472-1501190572782"><p>[1, 2, 10, 4]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5472" id="5472-1501190578415" value="1501190578415" data-quiz-answer-id="1501190578415" data-quiz-question-id="5472" disabled="disabled" />
  <label for="5472-1501190578415"><p>[1, 2, 3, 4]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5472" id="5472-1501190600557" value="1501190600557" data-quiz-answer-id="1501190600557" data-quiz-question-id="5472" disabled="disabled" />
  <label for="5472-1501190600557"><p>a</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5472" id="5472-1501190741455" value="1501190741455" data-quiz-answer-id="1501190741455" data-quiz-question-id="5472" disabled="disabled" />
  <label for="5472-1501190741455"><p>b</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5473" data-position="10">
            <div class=" clearfix" id="quiz_question-5473">

    <h4 class="quiz_question">

        Question #9
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; a = [1, 2, 3, 4]
&gt;&gt;&gt; b = a
&gt;&gt;&gt; a[2] = 10
&gt;&gt;&gt; b
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5473">
                <li class="">

  <input type="radio" name="5473" id="5473-1501190584759" value="1501190584759" data-quiz-answer-id="1501190584759" data-quiz-question-id="5473" disabled="disabled" />
  <label for="5473-1501190584759"><p>[1]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5473" id="5473-1501190605356" value="1501190605356" data-quiz-answer-id="1501190605356" data-quiz-question-id="5473" disabled="disabled" checked="checked" />
  <label for="5473-1501190605356"><p>[1, 2, 10, 4]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5473" id="5473-1501190608080" value="1501190608080" data-quiz-answer-id="1501190608080" data-quiz-question-id="5473" disabled="disabled" />
  <label for="5473-1501190608080"><p>[1, 2, 3, 4]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5473" id="5473-1501190610219" value="1501190610219" data-quiz-answer-id="1501190610219" data-quiz-question-id="5473" disabled="disabled" />
  <label for="5473-1501190610219"><p>a</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5473" id="5473-1501190730646" value="1501190730646" data-quiz-answer-id="1501190730646" data-quiz-question-id="5473" disabled="disabled" />
  <label for="5473-1501190730646"><p>b</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>

      </section>
    </div>
  </div>



          <h2 class="gap">Tasks</h2>

    <div data-role="task19380" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-19380">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Print a list of integers
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a function that prints all integers of a list.</p>

<ul>
<li>Prototype: <code>def print_list_integer(my_list=[]):</code></li>
<li>Format: one integer per line. See example</li>
<li>You are not allowed to import any module</li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to cast integers into strings</li>
<li>You have to use <code>str.format()</code> to print integers</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__(&#39;0-print_list_integer&#39;).print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-data_structures</code></li>
            <li>File: <code>0-print_list_integer.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19380" data-batch-id="843" data-toggle="modal" data-target="#task-19380-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19380-users-done-modal" data-task-id="19380" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "0. Print a list of integers"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19380-score-info-score">0</span>/21
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19381" data-position="2" id="task-num-1">
      <div class="panel panel-default task-card " id="task-19381">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Secure access to an element in a list
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a function that retrieves an element from a list.</p>

<ul>
<li>Prototype: <code>def element_at(my_list, idx):</code></li>
<li>If <code>idx</code> is negative, the function should return <code>None</code></li>
<li>If <code>idx</code> is out of range (&gt; of number of element in <code>my_list</code>), the function should return <code>None</code> </li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>try/except</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__(&#39;1-element_at&#39;).element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print(&quot;Element at index {:d} is {}&quot;.format(idx, element_at(my_list, idx)))

guillaume@ubuntu:~/$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-data_structures</code></li>
            <li>File: <code>1-element_at.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19381" data-batch-id="843" data-toggle="modal" data-target="#task-19381-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19381-users-done-modal" data-task-id="19381" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "1. Secure access to an element in a list"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19381-score-info-score">0</span>/12
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19382" data-position="3" id="task-num-2">
      <div class="panel panel-default task-card " id="task-19382">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Replace element
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a function that replaces an element of a list at a specific position.</p>

<ul>
<li>Prototype: <code>def replace_in_list(my_list, idx, element):</code></li>
<li>If <code>idx</code> is negative, the function should not modify anything, and returns the original list</li>
<li>If <code>idx</code> is out of range (&gt; of number of element in <code>my_list</code>), the function should not modify anything, and returns the original list</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>try/except</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__(&#39;2-replace_in_list&#39;).replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-data_structures</code></li>
            <li>File: <code>2-replace_in_list.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19382" data-batch-id="843" data-toggle="modal" data-target="#task-19382-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19382-users-done-modal" data-task-id="19382" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "2. Replace element"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19382-score-info-score">0</span>/12
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19383" data-position="4" id="task-num-3">
      <div class="panel panel-default task-card " id="task-19383">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Print a list of integers... in reverse!
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a function that prints all integers of a list, in reverse order.</p>

<ul>
<li>Prototype: <code>def print_reversed_list_integer(my_list=[]):</code></li>
<li>Format: one integer per line. See example</li>
<li>You are not allowed to import any module</li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to cast integers into strings</li>
<li>You have to use <code>str.format()</code> to print integers</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__(&#39;3-print_reversed_list_integer&#39;).print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

guillaume@ubuntu:~/$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-data_structures</code></li>
            <li>File: <code>3-print_reversed_list_integer.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19383" data-batch-id="843" data-toggle="modal" data-target="#task-19383-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19383-users-done-modal" data-task-id="19383" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "3. Print a list of integers... in reverse!"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19383-score-info-score">0</span>/10
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19384" data-position="5" id="task-num-4">
      <div class="panel panel-default task-card " id="task-19384">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Replace in a copy
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a function that replaces an element in a list at a specific position without modifying the original list.</p>

<ul>
<li>Prototype: <code>def new_in_list(my_list, idx, element):</code></li>
<li>If <code>idx</code> is negative, the function should return a copy of the original <code>list</code></li>
<li>If <code>idx</code> is out of range (&gt; of number of element in <code>my_list</code>), the function should return a copy of the original <code>list</code></li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>try/except</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__(&#39;4-new_in_list&#39;).new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-data_structures</code></li>
            <li>File: <code>4-new_in_list.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19384" data-batch-id="843" data-toggle="modal" data-target="#task-19384-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19384-users-done-modal" data-task-id="19384" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "4. Replace in a copy"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19384-score-info-score">0</span>/12
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19385" data-position="6" id="task-num-5">
      <div class="panel panel-default task-card " id="task-19385">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Can you C me now?
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a function that removes all characters <code>c</code> and <code>C</code> from a string.</p>

<ul>
<li>Prototype: <code>def no_c(my_string):</code></li>
<li>The function should return the new string</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>str.replace()</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
no_c = __import__(&#39;5-no_c&#39;).no_c

print(no_c(&quot;Best School&quot;))
print(no_c(&quot;Chicago&quot;))
print(no_c(&quot;C is fun!&quot;))

guillaume@ubuntu:~/$ ./5-main.py
Best Shool
hiago
 is fun!
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-data_structures</code></li>
            <li>File: <code>5-no_c.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19385" data-batch-id="843" data-toggle="modal" data-target="#task-19385-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19385-users-done-modal" data-task-id="19385" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "5. Can you C me now?"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19385-score-info-score">0</span>/11
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19386" data-position="7" id="task-num-6">
      <div class="panel panel-default task-card " id="task-19386">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. Lists of lists = Matrix
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a function that prints a matrix of integers.</p>

<ul>
<li>Prototype: <code>def print_matrix_integer(matrix=[[]]):</code></li>
<li>Format: see example</li>
<li>You are not allowed to import any module</li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to cast integers into strings</li>
<li>You have to use <code>str.format()</code> to print integers</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__(&#39;6-print_matrix_integer&#39;).print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print(&quot;--&quot;)
print_matrix_integer()

guillaume@ubuntu:~/$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-data_structures</code></li>
            <li>File: <code>6-print_matrix_integer.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19386" data-batch-id="843" data-toggle="modal" data-target="#task-19386-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19386-users-done-modal" data-task-id="19386" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "6. Lists of lists = Matrix"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19386-score-info-score">0</span>/11
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19387" data-position="8" id="task-num-7">
      <div class="panel panel-default task-card " id="task-19387">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      7. Tuples addition
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a function that adds 2 tuples.</p>

<ul>
<li>Prototype: <code>def add_tuple(tuple_a=(), tuple_b=()):</code></li>
<li>Returns a tuple with 2 integers:

<ul>
<li>The first element should be the addition of the first element of each argument</li>
<li>The second element should be the addition of the second element of each argument</li>
</ul></li>
<li>You are not allowed to import any module</li>
<li>You can assume that the two tuples will only contain integers</li>
<li>If a tuple is smaller than 2, use the value <code>0</code> for each missing integer</li>
<li>If a tuple is bigger than 2, use only the first 2 integers</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__(&#39;7-add_tuple&#39;).add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

guillaume@ubuntu:~/$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-data_structures</code></li>
            <li>File: <code>7-add_tuple.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19387" data-batch-id="843" data-toggle="modal" data-target="#task-19387-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19387-users-done-modal" data-task-id="19387" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "7. Tuples addition"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19387-score-info-score">0</span>/15
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19388" data-position="9" id="task-num-8">
      <div class="panel panel-default task-card " id="task-19388">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      8. More returns!
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a function that returns a tuple with the length of a string and its first character.</p>

<ul>
<li>Prototype: <code>def multiple_returns(sentence):</code></li>
<li>If the sentence is empty, the first character should be equal to <code>None</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
multiple_returns = __import__(&#39;8-multiple_returns&#39;).multiple_returns

sentence = &quot;At school, I learnt C!&quot;
length, first = multiple_returns(sentence)
print(&quot;Length: {:d} - First character: {}&quot;.format(length, first))

guillaume@ubuntu:~/$ ./8-main.py
Length: 22 - First character: A
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-data_structures</code></li>
            <li>File: <code>8-multiple_returns.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19388" data-batch-id="843" data-toggle="modal" data-target="#task-19388-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19388-users-done-modal" data-task-id="19388" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "8. More returns!"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19388-score-info-score">0</span>/9
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19389" data-position="10" id="task-num-9">
      <div class="panel panel-default task-card " id="task-19389">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      9. Find the max
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a function that finds the biggest integer of a list. </p>

<ul>
<li>Prototype: <code>def max_integer(my_list=[]):</code></li>
<li>If the list is empty, return <code>None</code></li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use the builtin <code>max()</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
max_integer = __import__(&#39;9-max_integer&#39;).max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print(&quot;Max: {}&quot;.format(max_value))

guillaume@ubuntu:~/$ ./9-main.py
Max: 90
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-data_structures</code></li>
            <li>File: <code>9-max_integer.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19389" data-batch-id="843" data-toggle="modal" data-target="#task-19389-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19389-users-done-modal" data-task-id="19389" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "9. Find the max"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19389-score-info-score">0</span>/12
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19390" data-position="11" id="task-num-10">
      <div class="panel panel-default task-card " id="task-19390">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      10. Only by 2
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a function that finds all multiples of 2 in a list.</p>

<ul>
<li>Prototype: <code>def divisible_by_2(my_list=[]):</code></li>
<li>Return a new list with <code>True</code> or <code>False</code>, depending on whether the integer at the same position in the original list is a multiple of 2</li>
<li>The new list should have the same size as the original list</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 10-main.py
#!/usr/bin/python3
divisible_by_2 = __import__(&#39;10-divisible_by_2&#39;).divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i &lt; len(list_result):
    print(&quot;{:d} {:s} divisible by 2&quot;.format(my_list[i], &quot;is&quot; if list_result[i] else &quot;is not&quot;))
    i += 1

guillaume@ubuntu:~/$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-data_structures</code></li>
            <li>File: <code>10-divisible_by_2.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19390" data-batch-id="843" data-toggle="modal" data-target="#task-19390-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19390-users-done-modal" data-task-id="19390" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "10. Only by 2"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19390-score-info-score">0</span>/9
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19398" data-position="12" id="task-num-11">
      <div class="panel panel-default task-card " id="task-19398">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      11. Delete at
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a function that deletes the item at a specific position in a list.</p>

<ul>
<li>Prototype: <code>def delete_at(my_list=[], idx=0):</code></li>
<li>If <code>idx</code> is negative or out of range, nothing change (returns the same list)</li>
<li>You are not allowed to use <code>pop()</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 11-main.py
#!/usr/bin/python3
delete_at = __import__(&#39;11-delete_at&#39;).delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-data_structures</code></li>
            <li>File: <code>11-delete_at.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19398" data-batch-id="843" data-toggle="modal" data-target="#task-19398-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19398-users-done-modal" data-task-id="19398" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "11. Delete at"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19398-score-info-score">0</span>/11
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19399" data-position="13" id="task-num-12">
      <div class="panel panel-default task-card " id="task-19399">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      12. Switch
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="9546"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Complete the source code in order to switch value of <code>a</code> and <code>b</code></p>

<ul>
<li>You can find the source code <a href="/rltoken/9viUCbnIwdfsOPV_UrvIRA" title="here" target="_blank">here</a></li>
<li>Your code should be inserted where the comment is (line 4)</li>
<li>Your program should be exactly 5 lines long</li>
</ul>

<pre><code>guillaume@ubuntu:~/py/$ ./12-switch.py
a=10 - b=89
guillaume@ubuntu:~/py/$ wc -l 12-switch.py
5 12-switch.py
guillaume@ubuntu:~/py/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-data_structures</code></li>
            <li>File: <code>12-switch.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19399" data-batch-id="843" data-toggle="modal" data-target="#task-19399-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19399-users-done-modal" data-task-id="19399" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "12. Switch"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19399-score-info-score">0</span>/11
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>



          <div class="gap">
  <div data-react-class="projects/ProjectReview" data-react-props="{&quot;correction&quot;:{&quot;statusURI&quot;:&quot;/corrections/1023983/status_self_paced.json&quot;,&quot;startReviewURI&quot;:&quot;/corrections/1023983/start_auto_review_self_paced.json&quot;},&quot;csrfToken&quot;:&quot;znbI6Z-nTRSAoHMua_eSDaISas8WUIs2s33tBI85_DTx5gTHDMxHwsVuJns86m-azh_XT6k7eM4pFbSJhy6bcw&quot;,&quot;nextProject&quot;:{&quot;details&quot;:{&quot;curriculum_completed&quot;:false,&quot;message&quot;:&quot;Next project: Python - More Data Structures: Set, Dictionary&quot;,&quot;uri&quot;:&quot;/projects/2121&quot;},&quot;fetchURI&quot;:&quot;/projects/2120/next&quot;},&quot;pollingInterval&quot;:10000,&quot;progress&quot;:{&quot;auto_review&quot;:{&quot;can_execute&quot;:true,&quot;completion&quot;:{&quot;count&quot;:0,&quot;is_completed&quot;:false,&quot;percentage&quot;:0.0},&quot;inability_to_execute_reason&quot;:null},&quot;tasks&quot;:[{&quot;id&quot;:19380,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:21,&quot;score&quot;:0}},{&quot;id&quot;:19381,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:12,&quot;score&quot;:0}},{&quot;id&quot;:19382,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:12,&quot;score&quot;:0}},{&quot;id&quot;:19383,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:10,&quot;score&quot;:0}},{&quot;id&quot;:19384,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:12,&quot;score&quot;:0}},{&quot;id&quot;:19385,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:11,&quot;score&quot;:0}},{&quot;id&quot;:19386,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:11,&quot;score&quot;:0}},{&quot;id&quot;:19387,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:15,&quot;score&quot;:0}},{&quot;id&quot;:19388,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:9,&quot;score&quot;:0}},{&quot;id&quot;:19389,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:12,&quot;score&quot;:0}},{&quot;id&quot;:19390,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:9,&quot;score&quot;:0}},{&quot;id&quot;:19398,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:11,&quot;score&quot;:0}},{&quot;id&quot;:19399,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:11,&quot;score&quot;:0}}],&quot;summary&quot;:{&quot;completion&quot;:0.0,&quot;score&quot;:{&quot;mandatory&quot;:null,&quot;optional&quot;:null}},&quot;can_skip&quot;:true,&quot;can_start_peer_review&quot;:false},&quot;peerReview&quot;:null,&quot;project&quot;:{&quot;completion&quot;:0.0,&quot;id&quot;:2120,&quot;index&quot;:0,&quot;isAccessible&quot;:true,&quot;isOptional&quot;:false,&quot;imagePath&quot;:&quot;/assets/pathway/003_color-0c5b38973bfe29fff8dd86f65a213ea2d2499a7d0d9e4549f440c50dc84c9618.png&quot;,&quot;name&quot;:&quot;Python - Data Structures: Lists, Tuples&quot;,&quot;score&quot;:{&quot;mandatory&quot;:0.0,&quot;optional&quot;:0.0},&quot;tasksCount&quot;:0},&quot;skipURI&quot;:&quot;/corrections/1023983/skip&quot;,&quot;taskLevelReviewTypeHumanized&quot;:&quot;Your score will be updated as you progress.&quot;}" data-react-cache-id="projects/ProjectReview-0"></div>
</div>



          <div class="modal fade" id="container-specs-modal"><div class="modal-dialog modal-lg"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button><h4 class="modal-title">Recommended Sandbox</h4></div><div class="modal-body"><div data-react-class="user_containers/ContainerSpecs" data-react-props="{&quot;containerModelName&quot;:&quot;Sandbox&quot;,&quot;containerSpecs&quot;:[{&quot;description&quot;:&quot;\u003cp\u003eBasic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Holberton Foundations\u003c/p\u003e\n&quot;,&quot;id&quot;:39,&quot;name&quot;:&quot;Ubuntu 20.04&quot;,&quot;online&quot;:true}],&quot;containersLimit&quot;:3,&quot;csrfToken&quot;:&quot;pxPLOPI2Gw3O3lk-TVq0_s4AW2-bUtN2mBwqza1eG5eYgwcWYV0R24sQDGsaR0lpog3m7yQ5II4CdHNApUl80A&quot;,&quot;startStatusURI&quot;:&quot;/user_containers/start_status.json&quot;,&quot;startURI&quot;:&quot;/user_containers/start.json&quot;}" data-react-cache-id="user_containers/ContainerSpecs-0"></div></div></div></div></div>
          <div class="modal fade" id="sandboxes-modal"><div class="modal-dialog modal-lg"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button><h4 class="modal-title">Recommended Sandboxes</h4></div><div class="modal-body"><div data-react-class="user_sandboxes/Sandboxes" data-react-props="{&quot;images&quot;:[{&quot;id&quot;:50,&quot;name&quot;:&quot;Ubuntu 18.04&quot;,&quot;aws_region&quot;:&quot;US East (N. Virginia)\t&quot;},{&quot;id&quot;:16,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;US East (N. Virginia)\t&quot;},{&quot;id&quot;:51,&quot;name&quot;:&quot;Ubuntu 18.04&quot;,&quot;aws_region&quot;:&quot;South America (São Paulo)&quot;},{&quot;id&quot;:17,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;South America (São Paulo)&quot;},{&quot;id&quot;:52,&quot;name&quot;:&quot;Ubuntu 18.04&quot;,&quot;aws_region&quot;:&quot;Europe (Paris)&quot;},{&quot;id&quot;:14,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;Europe (Paris)&quot;},{&quot;id&quot;:53,&quot;name&quot;:&quot;Ubuntu 18.04&quot;,&quot;aws_region&quot;:&quot;Asia Pacific (Sydney)&quot;},{&quot;id&quot;:18,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;Asia Pacific (Sydney)&quot;}],&quot;sandboxesUri&quot;:&quot;/user_sandboxes&quot;,&quot;csrfToken&quot;:&quot;UfYX7268vME572LmkNhZMcZ2IN4aSvN2cGSw_Ylzed1uZtvB_de2F3whN7PHxaSmqnudXqUhAI7qDOlwgWQemg&quot;,&quot;maxNumberOfContainers&quot;:2}" data-react-cache-id="user_sandboxes/Sandboxes-0"></div></div></div></div></div>

      <div class="d-flex justify-content-around align-items-center">
          <div>
            <a data-toggle="tooltip" title="Python - import &amp; modules" class="btn btn-primary" role="button" href="/projects/2175">Previous project</a>
          </div>
          <form action=/corrections/1023983/skip method="post">
            <input
              name="authenticity_token"
              type="hidden"
              value=OuTc9I5ZuXIgbl21QXqruqkjMcHhq5S1-n1IdtRiGHYFdBDaHTKzpGWgCOAWZ1YtxS6MQV7AZ01gFRH73HV_MQ
            />
            <button
              class="btn btn-warning"
              type="submit"
            >
              Next project
            </button>
          </form>
      </div>
  </div>
</div>

      </article>
    </main>
      <div class="modal fade" id="search-modal" tabindex="-1" role="dialog" aria-labelledby="search-modal-label">
    <div class="modal-dialog modal-md">
        <div class="modal-content">
            <div class="modal-header">
                <div id="search-bar-container">
    <input id="search-bar"
            type="text"
            name="hbtn-search-bar"
            placeholder="✨Start search by typing in this field✨">
</div>

            </div>
            <div class="modal-body">
                <div id="modal-spinner" class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div id="search-results-container">
</div>

            </div>
        </div>
    </div>
</div>

      <div class="modal fade" id="markdownGuideModal" tabindex="-1" role="dialog" aria-labelledby="markdownGuideModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-md">
    <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title">Markdown Guide</h4>
        </div>
        <div class="modal-body">
            <h4>Emphasis</h4>
<pre>**<strong>bold</strong>**
*<em>italics</em>*
~~<strike>strikethrough</strike>~~</pre>
<h4>Headers</h4>
<pre># Big header
## Medium header
### Small header
#### Tiny header</pre>
<h4>Lists</h4>
<pre>* Generic list item
* Generic list item
* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item</pre>
<h4>Links</h4>
<pre>[Text to display](http://www.example.com)</pre>
<h4>Quotes</h4>
<pre>> This is a quote.
> It can span multiple lines!</pre>
<h4>Images</h4>
<p>CSS style available: <code>width, height, opacity</code></p>
<pre>![](http://www.example.com/image.jpg)
![](http://www.example.com/image.jpg | width: 200px)
![](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)
</pre>
<h4>Tables</h4>
<pre>| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

<em>Or without aligning the columns...</em>

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |
</pre>
<h4>Displaying code</h4>
<pre>`var example = "hello!";`

<em>Or spanning multiple lines...</em>

```
var example = "hello!";
alert(example);
```</pre>
        </div>
    </div>
  </div>
</div>

      <script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

          ga('create',
            'UA-67152800-6',
            'auto', {
              userId: '9546'
            }
          );

        ga('send', 'pageview');

        $(document).ready(function() {
          ga(function(tracker) {
            var clientId = tracker.get('clientId');
            $('.ga-client-id').val(clientId);
          });
        });
      </script>

</body>
</html>

