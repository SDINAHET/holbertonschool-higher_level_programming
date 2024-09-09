<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="google" content="notranslate">
    <title>Project: Python - Test-driven development | Holberton Rennes, France Intranet</title>
      <link rel="stylesheet" href="https://use.typekit.net/xgz4ilr.css">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css">
      <link rel="stylesheet" media="all" href="/assets/application-82f828a36761ddaf87c87d57bfdf65ea423ccdbd071f956e4ad4b74a2662418c.css" />
      <script src="https://www.gstatic.com/charts/loader.js"></script>
      <meta name="action-cable-url" content="/cable" />
      <script src="/assets/application-08d13bb8d36999e13c0e8ca3172174cb5977d17ff1b0efa16aab65be73c6fa77.js"></script>
      <link rel="shortcut icon" type="image/x-icon" href="/favicon.ico" />
      <meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="ie7pIu3TXK0rrbh5kzESmdiR0KoRQ502lfbKG8BGTf22fiUMfrhWe25j7SzELO8OtJxtKq4obs4PnpOWyFEqug" />
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
          <div class="inner" style="background-image: url('https://s3.eu-west-3.amazonaws.com/hbtn.intranet/users/photos/000/009/546/thumb/Capture_d%E2%80%99%C3%A9cran_2024-06-03_111954.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240909%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20240909T114437Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=0acda302aa55ea36a455e6ddd63814a80e2302a08d1a25965b15307ef8e2b6dd')"></div>
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
          <div class="inner" style="background-image: url('https://s3.eu-west-3.amazonaws.com/hbtn.intranet/users/photos/000/009/546/thumb/Capture_d%E2%80%99%C3%A9cran_2024-06-03_111954.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240909%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20240909T114437Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=0acda302aa55ea36a455e6ddd63814a80e2302a08d1a25965b15307ef8e2b6dd')"></div>
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
    <div data-react-class="projects/ProjectHeader" data-react-props="{&quot;metadata&quot;:{&quot;level&quot;:&quot;Amateur&quot;,&quot;author&quot;:&quot;Guillaume&quot;,&quot;weight&quot;:1,&quot;migrated_to_sasheck&quot;:true,&quot;task_level_review_type&quot;:&quot;Your score will be updated as you progress.&quot;,&quot;correction&quot;:{&quot;released&quot;:true,&quot;requires_manual_correction&quot;:false}},&quot;project&quot;:{&quot;completion&quot;:0.0,&quot;id&quot;:2123,&quot;index&quot;:0,&quot;isAccessible&quot;:true,&quot;isOptional&quot;:false,&quot;imagePath&quot;:&quot;/assets/pathway/003_color-0c5b38973bfe29fff8dd86f65a213ea2d2499a7d0d9e4549f440c50dc84c9618.png&quot;,&quot;name&quot;:&quot;Python - Test-driven development&quot;,&quot;score&quot;:{&quot;mandatory&quot;:null,&quot;optional&quot;:null},&quot;tasksCount&quot;:2},&quot;slackLink&quot;:null,&quot;tags&quot;:[],&quot;videoRoomLink&quot;:null}" data-react-cache-id="projects/ProjectHeader-0"></div>
  </div>



    <div id="project_id" style="display: none" data-project-id="2123"></div>







      <div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/246/giphy-4.gif" alt="" loading='lazy' style="" /></p>

<h2>Background Context</h2>

<h3>Important notice on intranet checks for Python projects</h3>

<p>Starting from today:</p>

<ul>
<li>Based on the requirements of each task, <strong>you should always write the documentation (module(s) + function(s)) and tests first</strong>, before you actually code anything</li>
<li>The intranet checks for Python projects won&rsquo;t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case. <strong>But not in the implementation of them!</strong></li>
<li><strong>Don&rsquo;t trust the user</strong>, always think about all possible edge cases</li>
</ul>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/Hmd_LI8NZ-F2ymDxue5HCg" title="doctest — Test interactive Python examples" target="_blank">doctest — Test interactive Python examples</a> (<em>until &ldquo;26.2.3.7. Warnings&rdquo; included</em>)</li>
<li><a href="/rltoken/fbFfGNFU07L2yD0D1uc-Xg" title="doctest – Testing through documentation" target="_blank">doctest – Testing through documentation</a> </li>
<li><a href="/rltoken/LhbdUZYzqiP7cjxjE3rG3w" title="Unit Tests in Python" target="_blank">Unit Tests in Python</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/RMt2qsdC652WOJu2QyacaA" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome</li>
<li>What&rsquo;s an interactive test</li>
<li>Why tests are important</li>
<li>How to write Docstrings to create tests</li>
<li>How to write documentation for each module and function</li>
<li>What are the basic option flags to create tests</li>
<li>How to find edge cases</li>
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

<h3>Python Test Cases</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>All your test files should be inside a folder <code>tests</code></li>
<li>All your test files should be text files (extension: <code>.txt</code>)</li>
<li>All your tests should be executed by using this command: <code>python3 -m doctest ./tests/*</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your functions should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case &ndash; The Checker is checking for tests!</li>
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
          <div class="quiz_question_item_container" data-role="quiz_question5486" data-position="1">
            <div class=" clearfix" id="quiz_question-5486">

    <h4 class="quiz_question">

        Question #0
    </h4>

    <!-- Quiz question Body -->
    <p>Is this a standardized way to comment a function in Python?</p>

<pre><code>/* Addition function */
def add(a, b):
    return a + b
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5486">
                <li class="">

  <input type="radio" name="5486" id="5486-1503344951635" value="1503344951635" data-quiz-answer-id="1503344951635" data-quiz-question-id="5486" disabled="disabled" />
  <label for="5486-1503344951635"><p>Yes</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5486" id="5486-1503344954614" value="1503344954614" data-quiz-answer-id="1503344954614" data-quiz-question-id="5486" disabled="disabled" checked="checked" />
  <label for="5486-1503344954614"><p>No</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5487" data-position="2">
            <div class=" clearfix" id="quiz_question-5487">

    <h4 class="quiz_question">

        Question #1
    </h4>

    <!-- Quiz question Body -->
    <p>Is this a standardized way to comment a function in Python?</p>

<pre><code>&quot;&quot;&quot;&quot; Addition function &quot;&quot;&quot;
def add(a, b):
    return a + b
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5487">
                <li class="">

  <input type="radio" name="5487" id="5487-1503344960923" value="1503344960923" data-quiz-answer-id="1503344960923" data-quiz-question-id="5487" disabled="disabled" />
  <label for="5487-1503344960923"><p>Yes</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5487" id="5487-1503344963518" value="1503344963518" data-quiz-answer-id="1503344963518" data-quiz-question-id="5487" disabled="disabled" checked="checked" />
  <label for="5487-1503344963518"><p>No</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5488" data-position="3">
            <div class=" clearfix" id="quiz_question-5488">

    <h4 class="quiz_question">

        Question #2
    </h4>

    <!-- Quiz question Body -->
    <p>Is this a standardized way to comment a function in Python?</p>

<pre><code>##########
# Addition function
##########
def add(a, b):
    return a + b
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5488">
                <li class="">

  <input type="radio" name="5488" id="5488-1503344968632" value="1503344968632" data-quiz-answer-id="1503344968632" data-quiz-question-id="5488" disabled="disabled" />
  <label for="5488-1503344968632"><p>Yes</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5488" id="5488-1503344972406" value="1503344972406" data-quiz-answer-id="1503344972406" data-quiz-question-id="5488" disabled="disabled" checked="checked" />
  <label for="5488-1503344972406"><p>No</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5489" data-position="4">
            <div class=" clearfix" id="quiz_question-5489">

    <h4 class="quiz_question">

        Question #3
    </h4>

    <!-- Quiz question Body -->
    <p>Is this a standardized way to comment a function in Python?</p>

<pre><code>def add(a, b):
    &quot;&quot;&quot; Addition function &quot;&quot;&quot;
    return a + b
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5489">
                <li class="">

  <input type="radio" name="5489" id="5489-1503344976220" value="1503344976220" data-quiz-answer-id="1503344976220" data-quiz-question-id="5489" disabled="disabled" checked="checked" />
  <label for="5489-1503344976220"><p>Yes</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5489" id="5489-1503344978978" value="1503344978978" data-quiz-answer-id="1503344978978" data-quiz-question-id="5489" disabled="disabled" />
  <label for="5489-1503344978978"><p>No</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5490" data-position="5">
            <div class=" clearfix" id="quiz_question-5490">

    <h4 class="quiz_question">

        Question #4
    </h4>

    <!-- Quiz question Body -->
    <p>Is this module correctly commented?</p>

<pre><code>#!/usr/bin/python3
&quot;&quot;&quot;
    My calculation module
&quot;&quot;&quot;
import sys
...
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5490">
                <li class="">

  <input type="radio" name="5490" id="5490-1503344983799" value="1503344983799" data-quiz-answer-id="1503344983799" data-quiz-question-id="5490" disabled="disabled" checked="checked" />
  <label for="5490-1503344983799"><p>Yes</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5490" id="5490-1503344986684" value="1503344986684" data-quiz-answer-id="1503344986684" data-quiz-question-id="5490" disabled="disabled" />
  <label for="5490-1503344986684"><p>No</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5491" data-position="6">
            <div class=" clearfix" id="quiz_question-5491">

    <h4 class="quiz_question">

        Question #5
    </h4>

    <!-- Quiz question Body -->
    <p>Is this module correctly commented?</p>

<pre><code>#!/usr/bin/python3
import sys

&quot;&quot;&quot;
    My calculation module
&quot;&quot;&quot;
...
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5491">
                <li class="">

  <input type="radio" name="5491" id="5491-1503344991891" value="1503344991891" data-quiz-answer-id="1503344991891" data-quiz-question-id="5491" disabled="disabled" />
  <label for="5491-1503344991891"><p>Yes</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5491" id="5491-1503344994844" value="1503344994844" data-quiz-answer-id="1503344994844" data-quiz-question-id="5491" disabled="disabled" checked="checked" />
  <label for="5491-1503344994844"><p>No</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->
        <div class="alert alert-info">
            <h4>Tips:</h4>
            <p>Docstring must be before import statements</p>

        </div>

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5492" data-position="7">
            <div class=" clearfix" id="quiz_question-5492">

    <h4 class="quiz_question">

        Question #6
    </h4>

    <!-- Quiz question Body -->
    <p>Based on this code, what should all the test cases be? (select multiple)</p>

<pre><code>def uniq(list):
    &quot;&quot;&quot; Returns unique values of a list &quot;&quot;&quot;
    u_list = []
    for item in list:
        if item not in u_list:
            u_list.append(item)
    return u_list
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5492">
                <li class="">

  <input type="checkbox" name="5492" id="5492-1503345028280" value="1503345028280" data-quiz-answer-id="1503345028280" data-quiz-question-id="5492" disabled="disabled" checked="checked" />
  <label for="5492-1503345028280"><p>empty list</p>
</label>
</li>

                <li class="">

  <input type="checkbox" name="5492" id="5492-1503345034708" value="1503345034708" data-quiz-answer-id="1503345034708" data-quiz-question-id="5492" disabled="disabled" checked="checked" />
  <label for="5492-1503345034708"><p>list with one element (any type)</p>
</label>
</li>

                <li class="">

  <input type="checkbox" name="5492" id="5492-1503345045707" value="1503345045707" data-quiz-answer-id="1503345045707" data-quiz-question-id="5492" disabled="disabled" checked="checked" />
  <label for="5492-1503345045707"><p>list with 2 different element (same type)</p>
</label>
</li>

                <li class="">

  <input type="checkbox" name="5492" id="5492-1503345056728" value="1503345056728" data-quiz-answer-id="1503345056728" data-quiz-question-id="5492" disabled="disabled" checked="checked" />
  <label for="5492-1503345056728"><p>list with twice the same element (same type)</p>
</label>
</li>

                <li class="">

  <input type="checkbox" name="5492" id="5492-1503345080985" value="1503345080985" data-quiz-answer-id="1503345080985" data-quiz-question-id="5492" disabled="disabled" checked="checked" />
  <label for="5492-1503345080985"><p>list with more than 2 times the same element (same type)</p>
</label>
</li>

                <li class="">

  <input type="checkbox" name="5492" id="5492-1503345098717" value="1503345098717" data-quiz-answer-id="1503345098717" data-quiz-question-id="5492" disabled="disabled" checked="checked" />
  <label for="5492-1503345098717"><p>list with multiple types (integer, string, etc&hellip;)</p>
</label>
</li>

                <li class="">

  <input type="checkbox" name="5492" id="5492-1503345131400" value="1503345131400" data-quiz-answer-id="1503345131400" data-quiz-question-id="5492" disabled="disabled" checked="checked" />
  <label for="5492-1503345131400"><p>not a list argument (ex: passing a dictionary to the method)</p>
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

    <div data-role="task19430" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-19430">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Integers addition
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
    <p>Write a function that adds 2 integers.</p>

<ul>
<li>Prototype: <code>def add_integer(a, b=98):</code></li>
<li><code>a</code> and <code>b</code> must be integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>a must be an integer</code> or <code>b must be an integer</code></li>
<li><code>a</code> and <code>b</code> must be first casted to integers if they are float</li>
<li>Returns an integer: the addition of <code>a</code> and <code>b</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
add_integer = __import__(&#39;0-add_integer&#39;).add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, &quot;School&quot;))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/$ python3 -c &#39;print(__import__(&quot;0-add_integer&quot;).__doc__)&#39; | wc -l
5
guillaume@ubuntu:~/$ python3 -c &#39;print(__import__(&quot;0-add_integer&quot;).add_integer.__doc__)&#39; | wc -l
3
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
            <li>Directory: <code>python-test_driven_development</code></li>
            <li>File: <code>0-add_integer.py, tests/0-add_integer.txt</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19430" data-batch-id="843" data-toggle="modal" data-target="#task-19430-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19430-users-done-modal" data-task-id="19430" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "0. Integers addition"</h4>
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


      <button class="btn btn-default btn-sm" data-task-id="19430" data-toggle="modal" data-target="#task-test-correction-19430-correction-modal" id="task-num-0-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-19430-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "0. Integers addition"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="19430">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="19430">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="19430">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19430-score-info-score">0</span>/30
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19432" data-position="3" id="task-num-1">
      <div class="panel panel-default task-card " id="task-19432">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Divide a matrix
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
    <p>Write a function that divides all elements of a matrix.</p>

<ul>
<li>Prototype: <code>def matrix_divided(matrix, div):</code></li>
<li><code>matrix</code> must be a list of lists of integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>matrix must be a matrix (list of lists) of integers/floats</code></li>
<li>Each row of the <code>matrix</code> must be of the same size, otherwise raise a <code>TypeError</code> exception with the message <code>Each row of the matrix must have the same size</code></li>
<li><code>div</code> must be a number (integer or float), otherwise raise a <code>TypeError</code> exception with the message <code>div must be a number</code></li>
<li><code>div</code> can&rsquo;t be equal to <code>0</code>, otherwise raise a <code>ZeroDivisionError</code> exception with the message <code>division by zero</code></li>
<li>All elements of the matrix should be divided by <code>div</code>, rounded to 2 decimal places </li>
<li>Returns a new matrix</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
matrix_divided = __import__(&#39;2-matrix_divided&#39;).matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

guillaume@ubuntu:~/$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/$
</code></pre>

<p>Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.</p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-test_driven_development</code></li>
            <li>File: <code>2-matrix_divided.py, tests/2-matrix_divided.txt</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19432" data-batch-id="843" data-toggle="modal" data-target="#task-19432-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19432-users-done-modal" data-task-id="19432" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "1. Divide a matrix"</h4>
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


      <button class="btn btn-default btn-sm" data-task-id="19432" data-toggle="modal" data-target="#task-test-correction-19432-correction-modal" id="task-num-1-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-19432-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "1. Divide a matrix"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="19432">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="19432">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="19432">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19432-score-info-score">0</span>/39
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19433" data-position="4" id="task-num-2">
      <div class="panel panel-default task-card " id="task-19433">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Say my name
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
    <p>Write a function that prints <code>My name is &lt;first name&gt; &lt;last name&gt;</code></p>

<ul>
<li>Prototype: <code>def say_my_name(first_name, last_name=&quot;&quot;):</code></li>
<li><code>first_name</code> and <code>last_name</code> must be strings otherwise, raise a <code>TypeError</code> exception with the message <code>first_name must be a string</code> or <code>last_name must be a string</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
say_my_name = __import__(&#39;3-say_my_name&#39;).say_my_name

say_my_name(&quot;John&quot;, &quot;Smith&quot;)
say_my_name(&quot;Walter&quot;, &quot;White&quot;)
say_my_name(&quot;Bob&quot;)
try:
    say_my_name(12, &quot;White&quot;)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./3-main.py | cat -e
My name is John Smith$
My name is Walter White$
My name is Bob $
first_name must be a string$
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/$
</code></pre>

<p>Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.</p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-test_driven_development</code></li>
            <li>File: <code>3-say_my_name.py, tests/3-say_my_name.txt</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19433" data-batch-id="843" data-toggle="modal" data-target="#task-19433-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19433-users-done-modal" data-task-id="19433" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "2. Say my name"</h4>
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


      <button class="btn btn-default btn-sm" data-task-id="19433" data-toggle="modal" data-target="#task-test-correction-19433-correction-modal" id="task-num-2-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-19433-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "2. Say my name"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="19433">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="19433">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="19433">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19433-score-info-score">0</span>/24
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19434" data-position="5" id="task-num-3">
      <div class="panel panel-default task-card " id="task-19434">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Print square
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
    <p>Write a function that prints a square with the character <code>#</code>.</p>

<ul>
<li>Prototype: <code>def print_square(size):</code></li>
<li><code>size</code> is the size length of the square</li>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
<li>if <code>size</code> is a float and is less than 0, raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
print_square = __import__(&#39;4-print_square&#39;).print_square

print_square(4)
print(&quot;&quot;)
print_square(10)
print(&quot;&quot;)
print_square(0)
print(&quot;&quot;)
print_square(1)
print(&quot;&quot;)
try:
    print_square(-1)
except Exception as e:
    print(e)
print(&quot;&quot;)

guillaume@ubuntu:~/$ ./4-main.py
####
####
####
####

##########
##########
##########
##########
##########
##########
##########
##########
##########
##########


#

size must be &gt;= 0

guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/4-print_square.txt
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
            <li>Directory: <code>python-test_driven_development</code></li>
            <li>File: <code>4-print_square.py, tests/4-print_square.txt</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19434" data-batch-id="843" data-toggle="modal" data-target="#task-19434-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19434-users-done-modal" data-task-id="19434" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "3. Print square"</h4>
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


      <button class="btn btn-default btn-sm" data-task-id="19434" data-toggle="modal" data-target="#task-test-correction-19434-correction-modal" id="task-num-3-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-19434-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "3. Print square"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="19434">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="19434">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="19434">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19434-score-info-score">0</span>/25
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19435" data-position="6" id="task-num-4">
      <div class="panel panel-default task-card " id="task-19435">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Text indentation
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
    <p>Write a function that prints a text with 2 new lines after each of these characters: <code>.</code>, <code>?</code> and <code>:</code></p>

<ul>
<li>Prototype: <code>def text_indentation(text):</code></li>
<li><code>text</code> must be a string, otherwise raise a <code>TypeError</code> exception with the message <code>text must be a string</code></li>
<li>There should be no space at the beginning or at the end of each printed line</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
text_indentation = __import__(&#39;5-text_indentation&#39;).text_indentation

text_indentation(&quot;&quot;&quot;Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres&quot;&quot;&quot;)

guillaume@ubuntu:~/$ ./5-main.py | cat -e
Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
$
Quonam modo?$
$
Utrum igitur tibi litteram videor an totas paginas commovere?$
$
Non autem hoc:$
$
igitur ne illud quidem.$
$
Fortasse id optimum, sed ubi illud:$
$
Plus semper voluptatis?$
$
Teneo, inquit, finem illi videri nihil dolere.$
$
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
$
Si id dicis, vicimus.$
$
Inde sermone vario sex illa a Dipylo stadia confecimus.$
$
Sin aliud quid voles, postea.$
$
Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
$
Utinam quidem dicerent alium alio beatiorem! Iam ruinas videresguillaume@ubuntu:~/$
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/5-text_indentation.txt
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
            <li>Directory: <code>python-test_driven_development</code></li>
            <li>File: <code>5-text_indentation.py, tests/5-text_indentation.txt</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19435" data-batch-id="843" data-toggle="modal" data-target="#task-19435-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19435-users-done-modal" data-task-id="19435" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "4. Text indentation"</h4>
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


      <button class="btn btn-default btn-sm" data-task-id="19435" data-toggle="modal" data-target="#task-test-correction-19435-correction-modal" id="task-num-4-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-19435-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "4. Text indentation"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="19435">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="19435">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="19435">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19435-score-info-score">0</span>/24
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19438" data-position="7" id="task-num-5">
      <div class="panel panel-default task-card " id="task-19438">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Max integer - Unittest
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
    <p>Since the beginning you have been creating &ldquo;Interactive tests&rdquo;. For this exercise, you will add Unittests.</p>

<p>In this task, you will write unittests for the function <code>def max_integer(list=[]):</code>.</p>

<ul>
<li>Your test file should be inside a folder <code>tests</code></li>
<li>You have to use the <a href="/rltoken/0a3DSCMIMni_V7pgq1myLQ" title="unittest module" target="_blank">unittest module</a> </li>
<li>Your test file should be python files (extension: <code>.py</code>)</li>
<li>Your test file should be executed by using this command: <code>python3 -m unittest tests.6-max_integer_test</code> </li>
<li>All tests you make must be passable by the function below</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 6-max_integer.py
#!/usr/bin/python3
&quot;&quot;&quot;Module to find the max integer in a list
&quot;&quot;&quot;


def max_integer(list=[]):
    &quot;&quot;&quot;Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    &quot;&quot;&quot;
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i &lt; len(list):
        if list[i] &gt; result:
            result = list[i]
        i += 1
    return result

guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
max_integer = __import__(&#39;6-max_integer&#39;).max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ ./6-main.py
4
4
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ python3 -m unittest tests.6-max_integer_test 2&gt;&amp;1 | tail -1
OK
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ head -7 tests/6-max_integer_test.py
#!/usr/bin/python3
&quot;&quot;&quot;Unittest for max_integer([..])
&quot;&quot;&quot;
import unittest
max_integer = __import__(&#39;6-max_integer&#39;).max_integer

class TestMaxInteger(unittest.TestCase):
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
            <li>Directory: <code>python-test_driven_development</code></li>
            <li>File: <code>tests/6-max_integer_test.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19438" data-batch-id="843" data-toggle="modal" data-target="#task-19438-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19438-users-done-modal" data-task-id="19438" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "5. Max integer - Unittest"</h4>
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


      <button class="btn btn-default btn-sm" data-task-id="19438" data-toggle="modal" data-target="#task-test-correction-19438-correction-modal" id="task-num-5-check-code-btn">
          Review your work
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-19438-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "5. Max integer - Unittest"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="19438">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="19438">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="19438">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19438-score-info-score">0</span>/25
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>

    <p class="lg-gap">
      <a class="btn btn-primary btn-block" data-confirm="Are you sure? Make sure you focused on the mandatory tasks first" href="/projects/2123/unlock_optionals">Done with the mandatory tasks? Unlock 2 advanced tasks now!</a>
    </p>


          <div class="gap">
  <div data-react-class="projects/ProjectReview" data-react-props="{&quot;correction&quot;:{&quot;statusURI&quot;:&quot;/corrections/1023992/status_self_paced.json&quot;,&quot;startReviewURI&quot;:&quot;/corrections/1023992/start_auto_review_self_paced.json&quot;},&quot;csrfToken&quot;:&quot;JGlNxWrnPMWUXxzVqUdOlsj7euu9gDdpPacKNvfli3Ib-YHr-Yw2E9GRSYD-WrMBpPbHawLrxJGnz1O7__LsNQ&quot;,&quot;nextProject&quot;:{&quot;details&quot;:{&quot;curriculum_completed&quot;:false,&quot;message&quot;:&quot;Next project: Python - Classes and Objects&quot;,&quot;uri&quot;:&quot;/projects/2124&quot;},&quot;fetchURI&quot;:&quot;/projects/2123/next&quot;},&quot;pollingInterval&quot;:10000,&quot;progress&quot;:{&quot;auto_review&quot;:{&quot;can_execute&quot;:true,&quot;completion&quot;:{&quot;count&quot;:0,&quot;is_completed&quot;:false,&quot;percentage&quot;:0.0},&quot;inability_to_execute_reason&quot;:null},&quot;tasks&quot;:[{&quot;id&quot;:19430,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:30,&quot;score&quot;:0}},{&quot;id&quot;:19432,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:39,&quot;score&quot;:0}},{&quot;id&quot;:19433,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:24,&quot;score&quot;:0}},{&quot;id&quot;:19434,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:25,&quot;score&quot;:0}},{&quot;id&quot;:19435,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:24,&quot;score&quot;:0}},{&quot;id&quot;:19438,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:25,&quot;score&quot;:0}}],&quot;summary&quot;:{&quot;completion&quot;:0.0,&quot;score&quot;:{&quot;mandatory&quot;:null,&quot;optional&quot;:null}},&quot;can_skip&quot;:true,&quot;can_start_peer_review&quot;:false},&quot;peerReview&quot;:null,&quot;project&quot;:{&quot;completion&quot;:0.0,&quot;id&quot;:2123,&quot;index&quot;:0,&quot;isAccessible&quot;:true,&quot;isOptional&quot;:false,&quot;imagePath&quot;:&quot;/assets/pathway/003_color-0c5b38973bfe29fff8dd86f65a213ea2d2499a7d0d9e4549f440c50dc84c9618.png&quot;,&quot;name&quot;:&quot;Python - Test-driven development&quot;,&quot;score&quot;:{&quot;mandatory&quot;:null,&quot;optional&quot;:null},&quot;tasksCount&quot;:2},&quot;skipURI&quot;:&quot;/corrections/1023992/skip&quot;,&quot;taskLevelReviewTypeHumanized&quot;:&quot;Your score will be updated as you progress.&quot;}" data-react-cache-id="projects/ProjectReview-0"></div>
</div>



          <div class="modal fade" id="container-specs-modal"><div class="modal-dialog modal-lg"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button><h4 class="modal-title">Recommended Sandbox</h4></div><div class="modal-body"><div data-react-class="user_containers/ContainerSpecs" data-react-props="{&quot;containerModelName&quot;:&quot;Sandbox&quot;,&quot;containerSpecs&quot;:[{&quot;description&quot;:&quot;\u003cp\u003eBasic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Holberton Foundations\u003c/p\u003e\n&quot;,&quot;id&quot;:39,&quot;name&quot;:&quot;Ubuntu 20.04&quot;,&quot;online&quot;:true}],&quot;containersLimit&quot;:3,&quot;csrfToken&quot;:&quot;Mrf9p2UH2tCV-aFcW61hQTkI6wY28EB95_iXAuHnzZYNJzGJ9mzQBtA39AkMsJzWVQVWhombs4V9kM6P6fCq0Q&quot;,&quot;startStatusURI&quot;:&quot;/user_containers/start_status.json&quot;,&quot;startURI&quot;:&quot;/user_containers/start.json&quot;}" data-react-cache-id="user_containers/ContainerSpecs-0"></div></div></div></div></div>
          <div class="modal fade" id="sandboxes-modal"><div class="modal-dialog modal-lg"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button><h4 class="modal-title">Recommended Sandboxes</h4></div><div class="modal-body"><div data-react-class="user_sandboxes/Sandboxes" data-react-props="{&quot;images&quot;:[{&quot;id&quot;:50,&quot;name&quot;:&quot;Ubuntu 18.04&quot;,&quot;aws_region&quot;:&quot;US East (N. Virginia)\t&quot;},{&quot;id&quot;:16,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;US East (N. Virginia)\t&quot;},{&quot;id&quot;:51,&quot;name&quot;:&quot;Ubuntu 18.04&quot;,&quot;aws_region&quot;:&quot;South America (São Paulo)&quot;},{&quot;id&quot;:17,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;South America (São Paulo)&quot;},{&quot;id&quot;:52,&quot;name&quot;:&quot;Ubuntu 18.04&quot;,&quot;aws_region&quot;:&quot;Europe (Paris)&quot;},{&quot;id&quot;:14,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;Europe (Paris)&quot;},{&quot;id&quot;:53,&quot;name&quot;:&quot;Ubuntu 18.04&quot;,&quot;aws_region&quot;:&quot;Asia Pacific (Sydney)&quot;},{&quot;id&quot;:18,&quot;name&quot;:&quot;Ubuntu 22.04&quot;,&quot;aws_region&quot;:&quot;Asia Pacific (Sydney)&quot;}],&quot;sandboxesUri&quot;:&quot;/user_sandboxes&quot;,&quot;csrfToken&quot;:&quot;tZHkeusZ3VHDYLJ9R4Y2DrKrBf8Qin0mIzFoEtvWuGWKAShUeHLXh4au5ygQm8uZ3qa4f6_hjt65WTGf08HfIg&quot;,&quot;maxNumberOfContainers&quot;:2}" data-react-cache-id="user_sandboxes/Sandboxes-0"></div></div></div></div></div>

      <div class="d-flex justify-content-around align-items-center">
          <div>
            <a data-toggle="tooltip" title="Python - Exceptions" class="btn btn-primary" role="button" href="/projects/2122">Previous project</a>
          </div>
          <form action=/corrections/1023992/skip method="post">
            <input
              name="authenticity_token"
              type="hidden"
              value=_taoru3bx6UWgDT0HqUoCuw537g2HY_Q4jwepIGYMzLBRmSAfrDNc1NOYaFJuNWdgDRiOIl2fCh4VEcpiY9UdQ
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
