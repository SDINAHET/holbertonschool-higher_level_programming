<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="google" content="notranslate">
    <title>Project: Python - More Data Structures: Set, Dictionary | Holberton Rennes, France Intranet</title>
      <link rel="stylesheet" href="https://use.typekit.net/xgz4ilr.css">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css">
      <link rel="stylesheet" media="all" href="/assets/application-82f828a36761ddaf87c87d57bfdf65ea423ccdbd071f956e4ad4b74a2662418c.css" />
      <script src="https://www.gstatic.com/charts/loader.js"></script>
      <meta name="action-cable-url" content="/cable" />
      <script src="/assets/application-08d13bb8d36999e13c0e8ca3172174cb5977d17ff1b0efa16aab65be73c6fa77.js"></script>
      <link rel="shortcut icon" type="image/x-icon" href="/favicon.ico" />
      <meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="viLTEDutxrIYRL-8KSSIwh4Cwo5ld6yax20mh8P5VSOBsh8-qMbMZF2K6ul-OXVVcg9_DtocX2JdBX8Ky-4yZA" />
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
          <div class="inner" style="background-image: url('https://s3.eu-west-3.amazonaws.com/hbtn.intranet/users/photos/000/009/546/thumb/Capture_d%E2%80%99%C3%A9cran_2024-06-03_111954.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240909%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20240909T113038Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=99271265eb688f411a9ba64d64fae16541cafc44ff65b21f4484ddd045e3d8a9')"></div>
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
          <div class="inner" style="background-image: url('https://s3.eu-west-3.amazonaws.com/hbtn.intranet/users/photos/000/009/546/thumb/Capture_d%E2%80%99%C3%A9cran_2024-06-03_111954.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240909%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20240909T113038Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=99271265eb688f411a9ba64d64fae16541cafc44ff65b21f4484ddd045e3d8a9')"></div>
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
    <div data-react-class="projects/ProjectHeader" data-react-props="{&quot;metadata&quot;:{&quot;level&quot;:&quot;Novice&quot;,&quot;author&quot;:&quot;Guillaume&quot;,&quot;weight&quot;:1,&quot;migrated_to_sasheck&quot;:true,&quot;task_level_review_type&quot;:&quot;Your score will be updated as you progress.&quot;,&quot;correction&quot;:{&quot;released&quot;:false,&quot;requires_manual_correction&quot;:false}},&quot;project&quot;:{&quot;completion&quot;:0.0,&quot;id&quot;:2121,&quot;index&quot;:0,&quot;isAccessible&quot;:true,&quot;isOptional&quot;:false,&quot;imagePath&quot;:&quot;/assets/pathway/003_color-0c5b38973bfe29fff8dd86f65a213ea2d2499a7d0d9e4549f440c50dc84c9618.png&quot;,&quot;name&quot;:&quot;Python - More Data Structures: Set, Dictionary&quot;,&quot;score&quot;:{&quot;mandatory&quot;:0.0,&quot;optional&quot;:0.0},&quot;tasksCount&quot;:3},&quot;slackLink&quot;:null,&quot;tags&quot;:[],&quot;videoRoomLink&quot;:null}" data-react-cache-id="projects/ProjectHeader-0"></div>
  </div>



    <div id="project_id" style="display: none" data-project-id="2121"></div>







      <div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/K8JSw_eMWjw6EzmAL1S8bQ" title="Data structures" target="_blank">Data structures</a> </li>
<li><a href="/rltoken/JMc02-iMawLlxGCsnEalXA" title="Lambda, filter, reduce and map" target="_blank">Lambda, filter, reduce and map</a> </li>
<li><a href="/rltoken/NnWm29rFmdDcjcdRQX1tEw" title="Learn to Program 12 Lambda Map Filter Reduce" target="_blank">Learn to Program 12 Lambda Map Filter Reduce</a> </li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>python3</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/XpnbqLab-uqqsit6p5ifxA" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome</li>
<li>What are sets and how to use them</li>
<li>What are the most common methods of set and how to use them</li>
<li>When to use sets versus lists</li>
<li>How to iterate into a set</li>
<li>What are dictionaries and how to use them</li>
<li>When to use dictionaries versus lists or sets</li>
<li>What is a key in a dictionary</li>
<li>How to iterate over a dictionary</li>
<li>What is a lambda function</li>
<li>What are the map, reduce and filter functions</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

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
          <div class="quiz_question_item_container" data-role="quiz_question5474" data-position="1">
            <div class=" clearfix" id="quiz_question-5474">

    <h4 class="quiz_question">

        Question #0
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; a = { &#39;id&#39;: 89, &#39;name&#39;: &quot;John&quot; }
&gt;&gt;&gt; a[&#39;id&#39;]
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5474">
                <li class="">

  <input type="radio" name="5474" id="5474-1501191864320" value="1501191864320" data-quiz-answer-id="1501191864320" data-quiz-question-id="5474" disabled="disabled" />
  <label for="5474-1501191864320"><p>id</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5474" id="5474-1501191867639" value="1501191867639" data-quiz-answer-id="1501191867639" data-quiz-question-id="5474" disabled="disabled" />
  <label for="5474-1501191867639"><p>&lsquo;id&rsquo;</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5474" id="5474-1501191881231" value="1501191881231" data-quiz-answer-id="1501191881231" data-quiz-question-id="5474" disabled="disabled" />
  <label for="5474-1501191881231"><p>a[&lsquo;id&rsquo;]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5474" id="5474-1501191883470" value="1501191883470" data-quiz-answer-id="1501191883470" data-quiz-question-id="5474" disabled="disabled" checked="checked" />
  <label for="5474-1501191883470"><p>89</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5474" id="5474-1501191886293" value="1501191886293" data-quiz-answer-id="1501191886293" data-quiz-question-id="5474" disabled="disabled" />
  <label for="5474-1501191886293"><p>John</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5475" data-position="2">
            <div class=" clearfix" id="quiz_question-5475">

    <h4 class="quiz_question">

        Question #1
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; a = { &#39;id&#39;: 89, &#39;name&#39;: &quot;John&quot; }
&gt;&gt;&gt; a.get(&#39;id&#39;)
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5475">
                <li class="">

  <input type="radio" name="5475" id="5475-1501191912938" value="1501191912938" data-quiz-answer-id="1501191912938" data-quiz-question-id="5475" disabled="disabled" />
  <label for="5475-1501191912938"><p>id</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5475" id="5475-1501191922098" value="1501191922098" data-quiz-answer-id="1501191922098" data-quiz-question-id="5475" disabled="disabled" />
  <label for="5475-1501191922098"><p>&lsquo;id&rsquo;</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5475" id="5475-1501191925543" value="1501191925543" data-quiz-answer-id="1501191925543" data-quiz-question-id="5475" disabled="disabled" />
  <label for="5475-1501191925543"><p>a[&lsquo;id&rsquo;]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5475" id="5475-1501191927219" value="1501191927219" data-quiz-answer-id="1501191927219" data-quiz-question-id="5475" disabled="disabled" checked="checked" />
  <label for="5475-1501191927219"><p>89</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5475" id="5475-1501191961853" value="1501191961853" data-quiz-answer-id="1501191961853" data-quiz-question-id="5475" disabled="disabled" />
  <label for="5475-1501191961853"><p>John</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5476" data-position="3">
            <div class=" clearfix" id="quiz_question-5476">

    <h4 class="quiz_question">

        Question #2
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; a = { &#39;id&#39;: 89, &#39;name&#39;: &quot;John&quot; }
&gt;&gt;&gt; a.get(&#39;age&#39;)
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5476">
                <li class="">

  <input type="radio" name="5476" id="5476-1501191965878" value="1501191965878" data-quiz-answer-id="1501191965878" data-quiz-question-id="5476" disabled="disabled" />
  <label for="5476-1501191965878"><p>&lsquo;age&rsquo;</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5476" id="5476-1501191972525" value="1501191972525" data-quiz-answer-id="1501191972525" data-quiz-question-id="5476" disabled="disabled" />
  <label for="5476-1501191972525"><p>Not found</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5476" id="5476-1501191981713" value="1501191981713" data-quiz-answer-id="1501191981713" data-quiz-question-id="5476" disabled="disabled" />
  <label for="5476-1501191981713"><p>89</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5476" id="5476-1501191986301" value="1501191986301" data-quiz-answer-id="1501191986301" data-quiz-question-id="5476" disabled="disabled" />
  <label for="5476-1501191986301"><p>12</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5476" id="5476-1501191987883" value="1501191987883" data-quiz-answer-id="1501191987883" data-quiz-question-id="5476" disabled="disabled" checked="checked" />
  <label for="5476-1501191987883"><p>Nothing</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5477" data-position="4">
            <div class=" clearfix" id="quiz_question-5477">

    <h4 class="quiz_question">

        Question #3
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; a = { &#39;id&#39;: 89, &#39;name&#39;: &quot;John&quot; }
&gt;&gt;&gt; a.get(&#39;age&#39;, 0)
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5477">
                <li class="">

  <input type="radio" name="5477" id="5477-1501191999068" value="1501191999068" data-quiz-answer-id="1501191999068" data-quiz-question-id="5477" disabled="disabled" />
  <label for="5477-1501191999068"><p>&lsquo;age&rsquo;</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5477" id="5477-1501192003581" value="1501192003581" data-quiz-answer-id="1501192003581" data-quiz-question-id="5477" disabled="disabled" />
  <label for="5477-1501192003581"><p>Nothing</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5477" id="5477-1501192006928" value="1501192006928" data-quiz-answer-id="1501192006928" data-quiz-question-id="5477" disabled="disabled" checked="checked" />
  <label for="5477-1501192006928"><p>0</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5477" id="5477-1501192011054" value="1501192011054" data-quiz-answer-id="1501192011054" data-quiz-question-id="5477" disabled="disabled" />
  <label for="5477-1501192011054"><p>89</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5478" data-position="5">
            <div class=" clearfix" id="quiz_question-5478">

    <h4 class="quiz_question">

        Question #4
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; a = { &#39;id&#39;: 89, &#39;name&#39;: &quot;John&quot;, &#39;projects&#39;: [1, 2, 3, 4] }
&gt;&gt;&gt; a.get(&#39;projects&#39;)
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5478">
                <li class="">

  <input type="radio" name="5478" id="5478-1501192020609" value="1501192020609" data-quiz-answer-id="1501192020609" data-quiz-question-id="5478" disabled="disabled" />
  <label for="5478-1501192020609"><p>&lsquo;projects&rsquo;</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5478" id="5478-1501192024615" value="1501192024615" data-quiz-answer-id="1501192024615" data-quiz-question-id="5478" disabled="disabled" checked="checked" />
  <label for="5478-1501192024615"><p>[1, 2, 3, 4]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5478" id="5478-1501192031534" value="1501192031534" data-quiz-answer-id="1501192031534" data-quiz-question-id="5478" disabled="disabled" />
  <label for="5478-1501192031534"><p>[1]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5478" id="5478-1501192036072" value="1501192036072" data-quiz-answer-id="1501192036072" data-quiz-question-id="5478" disabled="disabled" />
  <label for="5478-1501192036072"><p>list</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5478" id="5478-1501192041939" value="1501192041939" data-quiz-answer-id="1501192041939" data-quiz-question-id="5478" disabled="disabled" />
  <label for="5478-1501192041939"><p>Nothing</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5479" data-position="6">
            <div class=" clearfix" id="quiz_question-5479">

    <h4 class="quiz_question">

        Question #5
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; a = { &#39;id&#39;: 89, &#39;name&#39;: &quot;John&quot;, &#39;projects&#39;: [1, 2, 3, 4] }
&gt;&gt;&gt; a.get(&#39;projects&#39;)[3]
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5479">
                <li class="">

  <input type="radio" name="5479" id="5479-1501192059933" value="1501192059933" data-quiz-answer-id="1501192059933" data-quiz-question-id="5479" disabled="disabled" checked="checked" />
  <label for="5479-1501192059933"><p>4</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5479" id="5479-1501192066092" value="1501192066092" data-quiz-answer-id="1501192066092" data-quiz-question-id="5479" disabled="disabled" />
  <label for="5479-1501192066092"><p>[4]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5479" id="5479-1501192080227" value="1501192080227" data-quiz-answer-id="1501192080227" data-quiz-question-id="5479" disabled="disabled" />
  <label for="5479-1501192080227"><p>[1, 2, 3, 4]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5479" id="5479-1501192082488" value="1501192082488" data-quiz-answer-id="1501192082488" data-quiz-question-id="5479" disabled="disabled" />
  <label for="5479-1501192082488"><p>3</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5479" id="5479-1501192088471" value="1501192088471" data-quiz-answer-id="1501192088471" data-quiz-question-id="5479" disabled="disabled" />
  <label for="5479-1501192088471"><p>[3]</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5480" data-position="7">
            <div class=" clearfix" id="quiz_question-5480">

    <h4 class="quiz_question">

        Question #6
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; a = { &#39;id&#39;: 89, &#39;name&#39;: &quot;John&quot;, &#39;projects&#39;: [1, 2, 3, 4], &#39;friends&#39;: [ { &#39;id&#39;: 82, &#39;name&#39;: &quot;Bob&quot; }, { &#39;id&#39;: 83, &#39;name&#39;: &quot;Amy&quot; } ] }
&gt;&gt;&gt; a.get(&#39;friends&#39;)[-1].get(&quot;name&quot;)
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5480">
                <li class="">

  <input type="radio" name="5480" id="5480-1501192106986" value="1501192106986" data-quiz-answer-id="1501192106986" data-quiz-question-id="5480" disabled="disabled" />
  <label for="5480-1501192106986"><p>89</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5480" id="5480-1501192114668" value="1501192114668" data-quiz-answer-id="1501192114668" data-quiz-question-id="5480" disabled="disabled" />
  <label for="5480-1501192114668"><p>[ { &lsquo;id&rsquo;: 82, &lsquo;name&rsquo;: &ldquo;Bob&rdquo; }, { &lsquo;id&rsquo;: 83, &lsquo;name&rsquo;: &ldquo;Amy&rdquo; } ]</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5480" id="5480-1501192120419" value="1501192120419" data-quiz-answer-id="1501192120419" data-quiz-question-id="5480" disabled="disabled" checked="checked" />
  <label for="5480-1501192120419"><p>Amy</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5480" id="5480-1501192124708" value="1501192124708" data-quiz-answer-id="1501192124708" data-quiz-question-id="5480" disabled="disabled" />
  <label for="5480-1501192124708"><p>Bob</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5480" id="5480-1501192136795" value="1501192136795" data-quiz-answer-id="1501192136795" data-quiz-question-id="5480" disabled="disabled" />
  <label for="5480-1501192136795"><p>Nothing</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5481" data-position="8">
            <div class=" clearfix" id="quiz_question-5481">

    <h4 class="quiz_question">

        Question #7
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; for i in range(0, 3):
&gt;&gt;&gt;     print(i, end=&quot; &quot;)
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5481">
                <li class="">

  <input type="radio" name="5481" id="5481-1501795196391" value="1501795196391" data-quiz-answer-id="1501795196391" data-quiz-question-id="5481" disabled="disabled" />
  <label for="5481-1501795196391"><p>1 2 3</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5481" id="5481-1501795201552" value="1501795201552" data-quiz-answer-id="1501795201552" data-quiz-question-id="5481" disabled="disabled" />
  <label for="5481-1501795201552"><p>0 1 2 3</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5481" id="5481-1501795204934" value="1501795204934" data-quiz-answer-id="1501795204934" data-quiz-question-id="5481" disabled="disabled" checked="checked" />
  <label for="5481-1501795204934"><p>0 1 2</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5482" data-position="9">
            <div class=" clearfix" id="quiz_question-5482">

    <h4 class="quiz_question">

        Question #8
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; for i in range(1, 4):
&gt;&gt;&gt;     print(i, end=&quot; &quot;)
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5482">
                <li class="">

  <input type="radio" name="5482" id="5482-1501795257783" value="1501795257783" data-quiz-answer-id="1501795257783" data-quiz-question-id="5482" disabled="disabled" checked="checked" />
  <label for="5482-1501795257783"><p>1 2 3</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5482" id="5482-1501795261185" value="1501795261185" data-quiz-answer-id="1501795261185" data-quiz-question-id="5482" disabled="disabled" />
  <label for="5482-1501795261185"><p>0 1 2 3</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5482" id="5482-1501795265499" value="1501795265499" data-quiz-answer-id="1501795265499" data-quiz-question-id="5482" disabled="disabled" />
  <label for="5482-1501795265499"><p>1 2 3 4</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5483" data-position="10">
            <div class=" clearfix" id="quiz_question-5483">

    <h4 class="quiz_question">

        Question #9
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; for i in [1, 2, 3, 4]:
&gt;&gt;&gt;     print(i, end=&quot; &quot;)
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5483">
                <li class="">

  <input type="radio" name="5483" id="5483-1501795290694" value="1501795290694" data-quiz-answer-id="1501795290694" data-quiz-question-id="5483" disabled="disabled" />
  <label for="5483-1501795290694"><p>0 1 2 3</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5483" id="5483-1501795300665" value="1501795300665" data-quiz-answer-id="1501795300665" data-quiz-question-id="5483" disabled="disabled" />
  <label for="5483-1501795300665"><p>0 1 2 3 5</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5483" id="5483-1501795303974" value="1501795303974" data-quiz-answer-id="1501795303974" data-quiz-question-id="5483" disabled="disabled" />
  <label for="5483-1501795303974"><p>1 2 3</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5483" id="5483-1501795307464" value="1501795307464" data-quiz-answer-id="1501795307464" data-quiz-question-id="5483" disabled="disabled" checked="checked" />
  <label for="5483-1501795307464"><p>1 2 3 4</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5484" data-position="11">
            <div class=" clearfix" id="quiz_question-5484">

    <h4 class="quiz_question">

        Question #10
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; for i in [1, 3, 4, 2]:
&gt;&gt;&gt;     print(i, end=&quot; &quot;)
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5484">
                <li class="">

  <input type="radio" name="5484" id="5484-1501795332939" value="1501795332939" data-quiz-answer-id="1501795332939" data-quiz-question-id="5484" disabled="disabled" />
  <label for="5484-1501795332939"><p>0 1 2 3</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5484" id="5484-1501795336042" value="1501795336042" data-quiz-answer-id="1501795336042" data-quiz-question-id="5484" disabled="disabled" />
  <label for="5484-1501795336042"><p>1 2 3 4</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5484" id="5484-1501795340814" value="1501795340814" data-quiz-answer-id="1501795340814" data-quiz-question-id="5484" disabled="disabled" checked="checked" />
  <label for="5484-1501795340814"><p>1 3 4 2</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5484" id="5484-1501795345132" value="1501795345132" data-quiz-answer-id="1501795345132" data-quiz-question-id="5484" disabled="disabled" />
  <label for="5484-1501795345132"><p>1 3 4 2 0</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5485" data-position="12">
            <div class=" clearfix" id="quiz_question-5485">

    <h4 class="quiz_question">

        Question #11
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; for i in [&quot;Hello&quot;, &quot;Holberton&quot;, &quot;School&quot;, 98]:
&gt;&gt;&gt;     print(i, end=&quot; &quot;)
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5485">
                <li class="">

  <input type="radio" name="5485" id="5485-1501795359980" value="1501795359980" data-quiz-answer-id="1501795359980" data-quiz-question-id="5485" disabled="disabled" />
  <label for="5485-1501795359980"><p>0 1 2 3</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5485" id="5485-1501795363179" value="1501795363179" data-quiz-answer-id="1501795363179" data-quiz-question-id="5485" disabled="disabled" />
  <label for="5485-1501795363179"><p>1 2 3 4</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5485" id="5485-1501795366983" value="1501795366983" data-quiz-answer-id="1501795366983" data-quiz-question-id="5485" disabled="disabled" checked="checked" />
  <label for="5485-1501795366983"><p>Hello Holberton School 98</p>
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

    <div data-role="task19401" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-19401">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Squared simple
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
    <p>Write a function that computes the square value of all integers of a matrix.</p>

<ul>
<li>Prototype: <code>def square_matrix_simple(matrix=[]):</code></li>
<li><code>matrix</code> is a 2 dimensional array</li>
<li>Returns a new matrix:

<ul>
<li>Same size as <code>matrix</code></li>
<li>Each value should be the square of the value of the input</li>
</ul></li>
<li>Initial matrix should not be modified</li>
<li>You are not allowed to import any module</li>
<li>You are allowed to use regular loops, <code>map</code>, etc.</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
square_matrix_simple = __import__(&#39;0-square_matrix_simple&#39;).square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

guillaume@ubuntu:~/$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
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
            <li>Directory: <code>python-more_data_structures</code></li>
            <li>File: <code>0-square_matrix_simple.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19401" data-batch-id="843" data-toggle="modal" data-target="#task-19401-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19401-users-done-modal" data-task-id="19401" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "0. Squared simple"</h4>
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
              <span id="task-19401-score-info-score">0</span>/11
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19402" data-position="2" id="task-num-1">
      <div class="panel panel-default task-card " id="task-19402">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Search and replace
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
    <p>Write a function that replaces all occurrences of an element by another in a new list.</p>

<ul>
<li>Prototype: <code>def search_replace(my_list, search, replace):</code></li>
<li><code>my_list</code> is the initial list</li>
<li><code>search</code> is the element to replace in the list</li>
<li><code>replace</code> is the new element</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
search_replace = __import__(&#39;1-search_replace&#39;).search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./1-main.py
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
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
            <li>Directory: <code>python-more_data_structures</code></li>
            <li>File: <code>1-search_replace.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19402" data-batch-id="843" data-toggle="modal" data-target="#task-19402-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19402-users-done-modal" data-task-id="19402" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "1. Search and replace"</h4>
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
              <span id="task-19402-score-info-score">0</span>/11
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19403" data-position="3" id="task-num-2">
      <div class="panel panel-default task-card " id="task-19403">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Unique addition
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
    <p>Write a function that adds all unique integers in a list (only once for each integer).</p>

<ul>
<li>Prototype: <code>def uniq_add(my_list=[]):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
uniq_add = __import__(&#39;2-uniq_add&#39;).uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print(&quot;Result: {:d}&quot;.format(result))

guillaume@ubuntu:~/$ ./2-main.py
Result: 15
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
            <li>Directory: <code>python-more_data_structures</code></li>
            <li>File: <code>2-uniq_add.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19403" data-batch-id="843" data-toggle="modal" data-target="#task-19403-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19403-users-done-modal" data-task-id="19403" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "2. Unique addition"</h4>
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
              <span id="task-19403-score-info-score">0</span>/13
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19404" data-position="4" id="task-num-3">
      <div class="panel panel-default task-card " id="task-19404">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Present in both
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
    <p>Write a function that returns a set of common elements in two sets.</p>

<ul>
<li>Prototype: <code>def common_elements(set_1, set_2):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
common_elements = __import__(&#39;3-common_elements&#39;).common_elements

set_1 = { &quot;Python&quot;, &quot;C&quot;, &quot;Javascript&quot; }
set_2 = { &quot;Bash&quot;, &quot;C&quot;, &quot;Ruby&quot;, &quot;Perl&quot; }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

guillaume@ubuntu:~/$ ./3-main.py
[&#39;C&#39;]
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
            <li>Directory: <code>python-more_data_structures</code></li>
            <li>File: <code>3-common_elements.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19404" data-batch-id="843" data-toggle="modal" data-target="#task-19404-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19404-users-done-modal" data-task-id="19404" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "3. Present in both"</h4>
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
              <span id="task-19404-score-info-score">0</span>/13
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19405" data-position="5" id="task-num-4">
      <div class="panel panel-default task-card " id="task-19405">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Only differents
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
    <p>Write a function that returns a set of all elements present in only one set.</p>

<ul>
<li>Prototype: <code>def only_diff_elements(set_1, set_2):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
only_diff_elements = __import__(&#39;4-only_diff_elements&#39;).only_diff_elements

set_1 = { &quot;Python&quot;, &quot;C&quot;, &quot;Javascript&quot; }
set_2 = { &quot;Bash&quot;, &quot;C&quot;, &quot;Ruby&quot;, &quot;Perl&quot; }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))

guillaume@ubuntu:~/$ ./4-main.py
[&#39;Bash&#39;, &#39;Javascript&#39;, &#39;Perl&#39;, &#39;Python&#39;, &#39;Ruby&#39;]
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
            <li>Directory: <code>python-more_data_structures</code></li>
            <li>File: <code>4-only_diff_elements.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19405" data-batch-id="843" data-toggle="modal" data-target="#task-19405-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19405-users-done-modal" data-task-id="19405" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "4. Only differents"</h4>
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
              <span id="task-19405-score-info-score">0</span>/13
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19406" data-position="6" id="task-num-5">
      <div class="panel panel-default task-card " id="task-19406">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Number of keys
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
    <p>Write a function that returns the number of keys in a dictionary.</p>

<ul>
<li>Prototype: <code>def number_keys(a_dictionary):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
number_keys = __import__(&#39;5-number_keys&#39;).number_keys

a_dictionary = { &#39;language&#39;: &quot;C&quot;, &#39;number&#39;: 13, &#39;track&#39;: &quot;Low level&quot; }
nb_keys = number_keys(a_dictionary)
print(&quot;Number of keys: {:d}&quot;.format(nb_keys))

guillaume@ubuntu:~/$ ./5-main.py
Number of keys: 3
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
            <li>Directory: <code>python-more_data_structures</code></li>
            <li>File: <code>5-number_keys.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19406" data-batch-id="843" data-toggle="modal" data-target="#task-19406-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19406-users-done-modal" data-task-id="19406" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "5. Number of keys"</h4>
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
              <span id="task-19406-score-info-score">0</span>/9
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19407" data-position="7" id="task-num-6">
      <div class="panel panel-default task-card " id="task-19407">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. Print sorted dictionary
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
    <p>Write a function that prints a dictionary by ordered keys.</p>

<ul>
<li>Prototype: <code>def print_sorted_dictionary(a_dictionary):</code></li>
<li>You can assume that all keys are strings</li>
<li>Keys should be sorted by alphabetic order</li>
<li>Only sort keys of the first level (don&rsquo;t sort keys of a dictionary inside the main dictionary)</li>
<li>Dictionary values can have any type</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
print_sorted_dictionary = __import__(&#39;6-print_sorted_dictionary&#39;).print_sorted_dictionary

a_dictionary = { &#39;language&#39;: &quot;C&quot;, &#39;Number&#39;: 89, &#39;track&#39;: &quot;Low level&quot;, &#39;ids&#39;: [1, 2, 3] }
print_sorted_dictionary(a_dictionary)

guillaume@ubuntu:~/$ ./6-main.py
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
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
            <li>Directory: <code>python-more_data_structures</code></li>
            <li>File: <code>6-print_sorted_dictionary.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19407" data-batch-id="843" data-toggle="modal" data-target="#task-19407-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19407-users-done-modal" data-task-id="19407" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "6. Print sorted dictionary"</h4>
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
              <span id="task-19407-score-info-score">0</span>/9
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19408" data-position="8" id="task-num-7">
      <div class="panel panel-default task-card " id="task-19408">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      7. Update dictionary
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
    <p>Write a function that replaces or adds key/value in a dictionary.</p>

<ul>
<li>Prototype: <code>def update_dictionary(a_dictionary, key, value):</code></li>
<li><code>key</code> argument will be always a string</li>
<li><code>value</code> argument will be any type</li>
<li>If a key exists in the dictionary, the value will be replaced</li>
<li>If a key doesn&rsquo;t exist in the dictionary, it will be created</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
update_dictionary = __import__(&#39;7-update_dictionary&#39;).update_dictionary
print_sorted_dictionary = __import__(&#39;6-print_sorted_dictionary&#39;).print_sorted_dictionary

a_dictionary = { &#39;language&#39;: &quot;C&quot;, &#39;number&#39;: 89, &#39;track&#39;: &quot;Low level&quot; }
new_dict = update_dictionary(a_dictionary, &#39;language&#39;, &quot;Python&quot;)
print_sorted_dictionary(new_dict)
print(&quot;--&quot;)
print_sorted_dictionary(a_dictionary)

print(&quot;--&quot;)
print(&quot;--&quot;)

new_dict = update_dictionary(a_dictionary, &#39;city&#39;, &quot;San Francisco&quot;)
print_sorted_dictionary(new_dict)
print(&quot;--&quot;)
print_sorted_dictionary(a_dictionary)

guillaume@ubuntu:~/$ ./7-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
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
            <li>Directory: <code>python-more_data_structures</code></li>
            <li>File: <code>7-update_dictionary.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19408" data-batch-id="843" data-toggle="modal" data-target="#task-19408-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19408-users-done-modal" data-task-id="19408" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "7. Update dictionary"</h4>
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
              <span id="task-19408-score-info-score">0</span>/11
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19409" data-position="9" id="task-num-8">
      <div class="panel panel-default task-card " id="task-19409">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      8. Simple delete by key
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
    <p>Write a function that deletes a key in a dictionary.</p>

<ul>
<li>Prototype: <code>def simple_delete(a_dictionary, key=&quot;&quot;):</code></li>
<li><code>key</code> argument will be always a string</li>
<li>If a key doesn&rsquo;t exist, the dictionary won&rsquo;t change</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
simple_delete = __import__(&#39;8-simple_delete&#39;).simple_delete
print_sorted_dictionary = \
    __import__(&#39;6-print_sorted_dictionary&#39;).print_sorted_dictionary

a_dictionary = { &#39;language&#39;: &quot;C&quot;, &#39;Number&#39;: 89, &#39;track&#39;: &quot;Low&quot;, &#39;ids&#39;: [1, 2, 3] }
new_dict = simple_delete(a_dictionary, &#39;track&#39;)
print_sorted_dictionary(a_dictionary)
print(&quot;--&quot;)
print_sorted_dictionary(new_dict)

print(&quot;--&quot;)
print(&quot;--&quot;)
new_dict = simple_delete(a_dictionary, &#39;c_is_fun&#39;)
print_sorted_dictionary(a_dictionary)
print(&quot;--&quot;)
print_sorted_dictionary(new_dict)

guillaume@ubuntu:~/$ ./8-main.py
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
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
            <li>Directory: <code>python-more_data_structures</code></li>
            <li>File: <code>8-simple_delete.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19409" data-batch-id="843" data-toggle="modal" data-target="#task-19409-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19409-users-done-modal" data-task-id="19409" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "8. Simple delete by key"</h4>
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
              <span id="task-19409-score-info-score">0</span>/9
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19410" data-position="10" id="task-num-9">
      <div class="panel panel-default task-card " id="task-19410">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      9. Multiply by 2
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
    <p>Write a function that returns a new dictionary with all values multiplied by 2</p>

<ul>
<li>Prototype: <code>def multiply_by_2(a_dictionary):</code></li>
<li>You can assume that all values are only integers</li>
<li>Returns a new dictionary</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
multiply_by_2 = __import__(&#39;9-multiply_by_2&#39;).multiply_by_2
print_sorted_dictionary = \
    __import__(&#39;6-print_sorted_dictionary&#39;).print_sorted_dictionary

a_dictionary = {&#39;John&#39;: 12, &#39;Alex&#39;: 8, &#39;Bob&#39;: 14, &#39;Mike&#39;: 14, &#39;Molly&#39;: 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print(&quot;--&quot;)
print_sorted_dictionary(new_dict)

guillaume@ubuntu:~/$ ./9-main.py
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
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
            <li>Directory: <code>python-more_data_structures</code></li>
            <li>File: <code>9-multiply_by_2.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19410" data-batch-id="843" data-toggle="modal" data-target="#task-19410-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19410-users-done-modal" data-task-id="19410" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "9. Multiply by 2"</h4>
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
              <span id="task-19410-score-info-score">0</span>/9
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19411" data-position="11" id="task-num-10">
      <div class="panel panel-default task-card " id="task-19411">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      10. Best score
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
    <p>Write a function that returns a key with the biggest integer value.</p>

<ul>
<li>Prototype: <code>def best_score(a_dictionary):</code></li>
<li>You can assume that all values are only integers</li>
<li>If no score found, return <code>None</code></li>
<li>You can assume all students have a different score</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 10-main.py
#!/usr/bin/python3
best_score = __import__(&#39;10-best_score&#39;).best_score

a_dictionary = {&#39;John&#39;: 12, &#39;Bob&#39;: 14, &#39;Mike&#39;: 14, &#39;Molly&#39;: 16, &#39;Adam&#39;: 10}
best_key = best_score(a_dictionary)
print(&quot;Best score: {}&quot;.format(best_key))

best_key = best_score(None)
print(&quot;Best score: {}&quot;.format(best_key))

guillaume@ubuntu:~/$ ./10-main.py
Best score: Molly
Best score: None
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
            <li>Directory: <code>python-more_data_structures</code></li>
            <li>File: <code>10-best_score.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19411" data-batch-id="843" data-toggle="modal" data-target="#task-19411-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19411-users-done-modal" data-task-id="19411" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "10. Best score"</h4>
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
              <span id="task-19411-score-info-score">0</span>/10
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19412" data-position="12" id="task-num-11">
      <div class="panel panel-default task-card " id="task-19412">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      11. Multiply by using map
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
    <p>Write a function that returns a list with all values multiplied by a number without using any loops.</p>

<ul>
<li>Prototype: <code>def multiply_list_map(my_list=[], number=0):</code></li>
<li>Returns a new list:

<ul>
<li>Same length as <code>my_list</code></li>
<li>Each value should be multiplied by <code>number</code></li>
</ul></li>
<li>Initial list should not be modified</li>
<li>You are not allowed to import any module</li>
<li>You have to use <code>map</code></li>
<li>Your file should be max 3 lines</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 11-main.py
#!/usr/bin/python3
multiply_list_map = __import__(&#39;11-multiply_list_map&#39;).multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./11-main.py
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
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
            <li>Directory: <code>python-more_data_structures</code></li>
            <li>File: <code>11-multiply_list_map.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19412" data-batch-id="843" data-toggle="modal" data-target="#task-19412-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19412-users-done-modal" data-task-id="19412" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "11. Multiply by using map"</h4>
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
              <span id="task-19412-score-info-score">0</span>/11
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19417" data-position="13" id="task-num-12">
      <div class="panel panel-default task-card " id="task-19417">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      12. Roman to Integer
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
    <p><strong>Technical interview preparation</strong>: </p>

<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
</ul>

<p>Create a function <code>def roman_to_int(roman_string):</code> that converts a <a href="/rltoken/COeilkCPRPmrPvaRSXcPyg" title="Roman numeral" target="_blank">Roman numeral</a> to an integer.</p>

<ul>
<li>You can assume the number will be between 1 to 3999.</li>
<li><code>def roman_to_int(roman_string)</code> must return an integer</li>
<li>If the <code>roman_string</code> is not a string or <code>None</code>, return 0</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 12-main.py
#!/usr/bin/python3
&quot;&quot;&quot; Roman to Integer test file
&quot;&quot;&quot;
roman_to_int = __import__(&#39;12-roman_to_int&#39;).roman_to_int

roman_number = &quot;X&quot;
print(&quot;{} = {}&quot;.format(roman_number, roman_to_int(roman_number)))

roman_number = &quot;VII&quot;
print(&quot;{} = {}&quot;.format(roman_number, roman_to_int(roman_number)))

roman_number = &quot;IX&quot;
print(&quot;{} = {}&quot;.format(roman_number, roman_to_int(roman_number)))

roman_number = &quot;LXXXVII&quot;
print(&quot;{} = {}&quot;.format(roman_number, roman_to_int(roman_number)))

roman_number = &quot;DCCVII&quot;
print(&quot;{} = {}&quot;.format(roman_number, roman_to_int(roman_number)))

guillaume@ubuntu:~/$ ./12-main.py
X = 10
VII = 7
IX = 9
LXXXVII = 87
DCCVII = 707
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
            <li>Directory: <code>python-more_data_structures</code></li>
            <li>File: <code>12-roman_to_int.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19417" data-batch-id="843" data-toggle="modal" data-target="#task-19417-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19417-users-done-modal" data-task-id="19417" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "12. Roman to Integer"</h4>
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
              <span id="task-19417-score-info-score">0</span>/10
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>

    <p class="lg-gap">
      <a class="btn btn-primary btn-block" data-confirm="Are you sure? Make sure you focused on the mandatory tasks first" href="/projects/2121/unlock_optionals">Done with the mandatory tasks? Unlock 3 advanced tasks now!</a>
    </p>


          <div class="gap">
  <div data-react-class="projects/ProjectReview" data-react-props="{&quot;correction&quot;:{&quot;statusURI&quot;:&quot;/corrections/1023986/status_self_paced.json&quot;,&quot;startReviewURI&quot;:&quot;/corrections/1023986/start_auto_review_self_paced.json&quot;},&quot;csrfToken&quot;:&quot;c54oguQVyuu7EkPq878vIDh3LV7Y8nBRrYmYnfOZBSNMDuSsd37APf7cFr-kotK3VHqQ3meZg6k34cEQ-45iZA&quot;,&quot;nextProject&quot;:{&quot;details&quot;:{&quot;curriculum_completed&quot;:false,&quot;message&quot;:&quot;Next project: Python - Exceptions&quot;,&quot;uri&quot;:&quot;/projects/2122&quot;},&quot;fetchURI&quot;:&quot;/projects/2121/next&quot;},&quot;pollingInterval&quot;:10000,&quot;progress&quot;:{&quot;auto_review&quot;:{&quot;can_execute&quot;:true,&quot;completion&quot;:{&quot;count&quot;:0,&quot;is_completed&quot;:false,&quot;percentage&quot;:0.0},&quot;inability_to_execute_reason&quot;:null},&quot;tasks&quot;:[{&quot;id&quot;:19401,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:11,&quot;score&quot;:0}},{&quot;id&quot;:19402,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:11,&quot;score&quot;:0}},{&quot;id&quot;:19403,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:13,&quot;score&quot;:0}},{&quot;id&quot;:19404,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:13,&quot;score&quot;:0}},{&quot;id&quot;:19405,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:13,&quot;score&quot;:0}},{&quot;id&quot;:19406,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:9,&quot;score&quot;:0}},{&quot;id&quot;:19407,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:9,&quot;score&quot;:0}},{&quot;id&quot;:19408,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:11,&quot;score&quot;:0}},{&quot;id&quot;:19409,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:9,&quot;score&quot;:0}},{&quot;id&quot;:19410,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:9,&quot;score&quot;:0}},{&quot;id&quot;:19411,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:10,&quot;score&quot;:0}},{&quot;id&quot;:19412,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:11,&quot;score&quot;:0}},{&quot;id&quot;:19417,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:10,&quot;score&quot;:0}}],&quot;summary&quot;:{&quot;completion&quot;:0.0,&quot;score&quot;:{&quot;mandatory&quot;:null,&quot;optional&quot;:null}},&quot;can_skip&quot;:true,&quot;can_start_peer_review&quot;:false},&quot;peerReview&quot;:null,&quot;project&quot;:{&quot;completion&quot;:0.0,&quot;id&quot;:2121,&quot;index&quot;:0,&quot;isAccessible&quot;:true,&quot;isOptional&quot;:false,&quot;imagePath&quot;:&quot;/assets/pathway/003_color-0c5b38973bfe29fff8dd86f65a213ea2d2499a7d0d9e4549f440c50dc84c9618.png&quot;,&quot;name&quot;:&quot;Python - More Data Structures: Set, Dictionary&quot;,&quot;score&quot;:{&quot;mandatory&quot;:0.0,&quot;optional&quot;:0.0},&quot;tasksCount&quot;:3},&quot;skipURI&quot;:&quot;/corrections/1023986/skip&quot;,&quot;taskLevelReviewTypeHumanized&quot;:&quot;Your score will be updated as you progress.&quot;}" data-react-cache-id="projects/ProjectReview-0"></div>
</div>



          <div class="modal fade" id="container-specs-modal"><div class="modal-dialog modal-lg"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button><h4 class="modal-title">Recommended Sandbox</h4></div><div class="modal-body"><div data-react-class="user_containers/ContainerSpecs" data-react-props="{&quot;containerModelName&quot;:&quot;Sandbox&quot;,&quot;containerSpecs&quot;:[{&quot;description&quot;:&quot;\u003cp\u003eBasic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Holberton Foundations\u003c/p\u003e\n&quot;,&quot;id&quot;:39,&quot;name&quot;:&quot;Ubuntu 20.04&quot;,&quot;online&quot;:true}],&quot;containersLimit&quot;:3,&quot;csrfToken&quot;:&quot;P2SApTtHmAG1bSoECdYEqd9j7R8OYAhV75ryFVl10IQA9EyLqCyS1_Cjf1Fey_k-s25Qn7EL-6118quYUWK3ww&quot;,&quot;startStatusURI&quot;:&quot;/user_containers/start_status.json&quot;,&quot;startURI&quot;:&quot;/user_containers/start.json&quot;}" data-react-cache-id="user_containers/ContainerSpecs-0"></div></div></div></div></div>
          <div class="modal fade" id="sandboxes-modal"><div class="modal-dialog modal-lg"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button><h4 class="modal-title">Recommended Sandboxes</h4></div><div class="modal-body"><div data-react-class="user_sandboxes/Sandboxes" data-react-props="{&quot;images&quot;:[{&quot;id&quot;:50,&quot;name&quot;:&quot;Ubuntu 18.04&quot;,&quot;aws_region&quot;:&quot;US East (N. Virginia)\t&quot;},{&quot;id&quot;:16,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;US East (N. Virginia)\t&quot;},{&quot;id&quot;:51,&quot;name&quot;:&quot;Ubuntu 18.04&quot;,&quot;aws_region&quot;:&quot;South America (São Paulo)&quot;},{&quot;id&quot;:17,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;South America (São Paulo)&quot;},{&quot;id&quot;:52,&quot;name&quot;:&quot;Ubuntu 18.04&quot;,&quot;aws_region&quot;:&quot;Europe (Paris)&quot;},{&quot;id&quot;:14,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;Europe (Paris)&quot;},{&quot;id&quot;:53,&quot;name&quot;:&quot;Ubuntu 18.04&quot;,&quot;aws_region&quot;:&quot;Asia Pacific (Sydney)&quot;},{&quot;id&quot;:18,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;Asia Pacific (Sydney)&quot;}],&quot;sandboxesUri&quot;:&quot;/user_sandboxes&quot;,&quot;csrfToken&quot;:&quot;9YRuYCxPR9_QCSFQn-_UhTl6ASOq6VIAMyFD8-cXpgfKFKJOvyRNCZXHdAXI8ikSVXe8oxWCofipSRp-7wDBQA&quot;,&quot;maxNumberOfContainers&quot;:2}" data-react-cache-id="user_sandboxes/Sandboxes-0"></div></div></div></div></div>

      <div class="d-flex justify-content-around align-items-center">
          <div>
            <a data-toggle="tooltip" title="Python - Data Structures: Lists, Tuples" class="btn btn-primary" role="button" href="/projects/2120">Previous project</a>
          </div>
          <form action=/corrections/1023986/skip method="post">
            <input
              name="authenticity_token"
              type="hidden"
              value=schfruJeV6P-bOYUpD192sZ5c3Iv2ajy-olYKp22hBSOWJOAcTVddbuis0HzIIBNqnTO8pCyWwpg4QGnlaHjUw
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
