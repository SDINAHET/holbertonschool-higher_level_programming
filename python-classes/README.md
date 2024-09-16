<div class="project row">
  <div class="col-xs-12 col-md-10 col-lg-8 contains-images">

      <div class="sm-gap">
    <div data-react-class="projects/ProjectHeader" data-react-props="{&quot;metadata&quot;:{&quot;level&quot;:&quot;Amateur&quot;,&quot;author&quot;:&quot;Guillaume&quot;,&quot;weight&quot;:1,&quot;migrated_to_sasheck&quot;:true,&quot;correction&quot;:{&quot;released&quot;:false,&quot;requires_manual_correction&quot;:false},&quot;task_level_review_type&quot;:&quot;Your score will be updated as you progress.&quot;},&quot;project&quot;:{&quot;completion&quot;:0.0,&quot;id&quot;:2124,&quot;index&quot;:0,&quot;isAccessible&quot;:true,&quot;isOptional&quot;:false,&quot;imagePath&quot;:&quot;/assets/pathway/003_color-0c5b38973bfe29fff8dd86f65a213ea2d2499a7d0d9e4549f440c50dc84c9618.png&quot;,&quot;name&quot;:&quot;Python - Classes and Objects&quot;,&quot;score&quot;:{&quot;mandatory&quot;:0.0,&quot;optional&quot;:0.0},&quot;tasksCount&quot;:3},&quot;slackLink&quot;:null,&quot;tags&quot;:[],&quot;videoRoomLink&quot;:null}" data-react-cache-id="projects/ProjectHeader-0"></div>
  </div>



    <div id="project_id" style="display: none" data-project-id="2124"></div>







      <div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/247/oop-meme.jpg" alt="" loading='lazy' style="" /></p>

<h2>Background Context</h2>

<p>It&rsquo;s VERY important that you read at least all the material that is listed below (and skip what we recommend you to skip, you will see them later in the curriculum). </p>

<p>As usual, make sure you type (never copy and paste), test, understand all examples shown in the following links (including those in the video), test again etc.
The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!</p>

<p>Read or watch the below resources in the order presented.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/5envVBirO286MdSZgZ4DoQ" title="Object Oriented Programming" target="_blank">Object Oriented Programming</a> (<em>Read everything until the paragraph &ldquo;Inheritance&rdquo; excluded. You do NOT have to learn about class attributes, <code>classmethod</code> and <code>staticmethod</code> yet</em>)</li>
<li><a href="/rltoken/sCdUrEsHLFH2NpUzI5Xx8w" title="Object-Oriented Programming" target="_blank">Object-Oriented Programming</a> (<em>Please *</em>be careful*<em>: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON&rsquo;T have to learn about class attributes), Methods, The <code>__init__</code> Method, &ldquo;Data Abstraction, Data Encapsulation, and Information Hiding,&rdquo; &ldquo;Public, Protected, and Private Attributes&rdquo;</em>)</li>
<li><a href="/rltoken/3B0RWILA_kSjK5udEbFt-A" title="Properties vs. Getters and Setters" target="_blank">Properties vs. Getters and Setters</a> </li>
<li><a href="/rltoken/5u8UhnaTWX2A-G7LICKCDw" title="Learn to Program 9 : Object Oriented Programming" target="_blank">Learn to Program 9 : Object Oriented Programming</a> </li>
<li><a href="/rltoken/cwqg7Ud04LTDsatPT17CaQ" title="Python Classes and Objects" target="_blank">Python Classes and Objects</a> </li>
<li><a href="/rltoken/6cZhWLe083CJERYLjAM0BQ" title="Object Oriented Programming" target="_blank">Object Oriented Programming</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/gwuqSZXS7ElRbiObQzDcTg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is OOP</li>
<li>&ldquo;first-class everything&rdquo;</li>
<li>What is a class</li>
<li>What is an object and an instance</li>
<li>What is the difference between a class and an object or instance</li>
<li>What is an attribute</li>
<li>What are and how to use public, protected and private attributes</li>
<li>What is <code>self</code></li>
<li>What is a method</li>
<li>What is the special <code>__init__</code> method and how to use it</li>
<li>What is Data Abstraction, Data Encapsulation, and Information Hiding</li>
<li>What is a property</li>
<li>What is the difference between an attribute and a property in Python</li>
<li>What is the Pythonic way to write getters and setters in Python</li>
<li>How to dynamically create arbitrary new attributes for existing instances of a class</li>
<li>How to bind attributes to object and classes</li>
<li>What is the <code>__dict__</code> of a class and/or instance of a class and what does it contain</li>
<li>How does Python find the attributes of an object or class</li>
<li>How to use the <code>getattr</code> function</li>
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
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

<h2>More Info</h2>

<p><strong>Documentation is now mandatory!</strong> Each module, class, and method must contain docstring as comments. <a href="/rltoken/WK6oRgAsdc3cSB4XHgE_1A" title="Example Google Style Python Docstrings" target="_blank">Example Google Style Python Docstrings</a></p>

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
          <div class="quiz_question_item_container" data-role="quiz_question5493" data-position="1">
            <div class=" clearfix" id="quiz_question-5493">

    <h4 class="quiz_question">

        Question #0
    </h4>

    <!-- Quiz question Body -->
    <p>In this following code, what is <code>User</code>?</p>

<pre><code>class User:
    id = 89
    name = &quot;no name&quot;
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5493">
                <li class="">

  <input type="radio" name="5493" id="5493-1501193339112" value="1501193339112" data-quiz-answer-id="1501193339112" data-quiz-question-id="5493" disabled="disabled" checked="checked" />
  <label for="5493-1501193339112"><p>A class</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5493" id="5493-1501193345297" value="1501193345297" data-quiz-answer-id="1501193345297" data-quiz-question-id="5493" disabled="disabled" />
  <label for="5493-1501193345297"><p>A string</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5493" id="5493-1501193351737" value="1501193351737" data-quiz-answer-id="1501193351737" data-quiz-question-id="5493" disabled="disabled" />
  <label for="5493-1501193351737"><p>An attribute</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5493" id="5493-1501193358124" value="1501193358124" data-quiz-answer-id="1501193358124" data-quiz-question-id="5493" disabled="disabled" />
  <label for="5493-1501193358124"><p>A method</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5493" id="5493-1501193367508" value="1501193367508" data-quiz-answer-id="1501193367508" data-quiz-question-id="5493" disabled="disabled" />
  <label for="5493-1501193367508"><p>An instance</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5494" data-position="2">
            <div class=" clearfix" id="quiz_question-5494">

    <h4 class="quiz_question">

        Question #1
    </h4>

    <!-- Quiz question Body -->
    <p>In this following code, what is <code>id</code>?</p>

<pre><code>class User:
    id = 89
    name = &quot;no name&quot;
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5494">
                <li class="">

  <input type="radio" name="5494" id="5494-1501193374600" value="1501193374600" data-quiz-answer-id="1501193374600" data-quiz-question-id="5494" disabled="disabled" />
  <label for="5494-1501193374600"><p>A public instance attribute</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5494" id="5494-1501193403131" value="1501193403131" data-quiz-answer-id="1501193403131" data-quiz-question-id="5494" disabled="disabled" checked="checked" />
  <label for="5494-1501193403131"><p>A public class attribute</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5494" id="5494-1501193411230" value="1501193411230" data-quiz-answer-id="1501193411230" data-quiz-question-id="5494" disabled="disabled" />
  <label for="5494-1501193411230"><p>A public class method</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5494" id="5494-1501193415397" value="1501193415397" data-quiz-answer-id="1501193415397" data-quiz-question-id="5494" disabled="disabled" />
  <label for="5494-1501193415397"><p>A public instance method</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5494" id="5494-1501193420965" value="1501193420965" data-quiz-answer-id="1501193420965" data-quiz-question-id="5494" disabled="disabled" />
  <label for="5494-1501193420965"><p>A private class attribute</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5494" id="5494-1501193433223" value="1501193433223" data-quiz-answer-id="1501193433223" data-quiz-question-id="5494" disabled="disabled" />
  <label for="5494-1501193433223"><p>A protected class attribute</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5495" data-position="3">
            <div class=" clearfix" id="quiz_question-5495">

    <h4 class="quiz_question">

        Question #2
    </h4>

    <!-- Quiz question Body -->
    <p>In this following code, what is <code>__password</code>?</p>

<pre><code>class User:
    id = 89
    name = &quot;no name&quot;
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5495">
                <li class="">

  <input type="radio" name="5495" id="5495-1501193439568" value="1501193439568" data-quiz-answer-id="1501193439568" data-quiz-question-id="5495" disabled="disabled" />
  <label for="5495-1501193439568"><p>A public class attribute</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5495" id="5495-1501193444546" value="1501193444546" data-quiz-answer-id="1501193444546" data-quiz-question-id="5495" disabled="disabled" />
  <label for="5495-1501193444546"><p>A public instance attribute</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5495" id="5495-1501193458722" value="1501193458722" data-quiz-answer-id="1501193458722" data-quiz-question-id="5495" disabled="disabled" />
  <label for="5495-1501193458722"><p>A protected class attribute</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5495" id="5495-1501193464986" value="1501193464986" data-quiz-answer-id="1501193464986" data-quiz-question-id="5495" disabled="disabled" />
  <label for="5495-1501193464986"><p>A protected instance attribute</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5495" id="5495-1501193470158" value="1501193470158" data-quiz-answer-id="1501193470158" data-quiz-question-id="5495" disabled="disabled" checked="checked" />
  <label for="5495-1501193470158"><p>A private class attribute</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5495" id="5495-1501193477329" value="1501193477329" data-quiz-answer-id="1501193477329" data-quiz-question-id="5495" disabled="disabled" />
  <label for="5495-1501193477329"><p>A private instance attribute</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5496" data-position="4">
            <div class=" clearfix" id="quiz_question-5496">

    <h4 class="quiz_question">

        Question #3
    </h4>

    <!-- Quiz question Body -->
    <p>In this following code, what is <code>is_new</code>?</p>

<pre><code>class User:
    id = 89
    name = &quot;no name&quot;
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5496">
                <li class="">

  <input type="radio" name="5496" id="5496-1501193491535" value="1501193491535" data-quiz-answer-id="1501193491535" data-quiz-question-id="5496" disabled="disabled" />
  <label for="5496-1501193491535"><p>A public class attribute</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5496" id="5496-1501193520326" value="1501193520326" data-quiz-answer-id="1501193520326" data-quiz-question-id="5496" disabled="disabled" checked="checked" />
  <label for="5496-1501193520326"><p>A public instance attribute</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5496" id="5496-1501193525293" value="1501193525293" data-quiz-answer-id="1501193525293" data-quiz-question-id="5496" disabled="disabled" />
  <label for="5496-1501193525293"><p>A protected class attribute</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5496" id="5496-1501193529672" value="1501193529672" data-quiz-answer-id="1501193529672" data-quiz-question-id="5496" disabled="disabled" />
  <label for="5496-1501193529672"><p>A protected instance attribute</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5496" id="5496-1501193534793" value="1501193534793" data-quiz-answer-id="1501193534793" data-quiz-question-id="5496" disabled="disabled" />
  <label for="5496-1501193534793"><p>A private class attribute</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5496" id="5496-1501193538923" value="1501193538923" data-quiz-answer-id="1501193538923" data-quiz-question-id="5496" disabled="disabled" />
  <label for="5496-1501193538923"><p>A private instance attribute</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5497" data-position="5">
            <div class=" clearfix" id="quiz_question-5497">

    <h4 class="quiz_question">

        Question #4
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; class User:
&gt;&gt;&gt;     id = 89
&gt;&gt;&gt;     name = &quot;no name&quot;
&gt;&gt;&gt;     __password = None
&gt;&gt;&gt;
&gt;&gt;&gt;     def __init__(self, new_name=None):
&gt;&gt;&gt;         self.is_new = True
&gt;&gt;&gt;         if new_name is not None:
&gt;&gt;&gt;             self.name = new_name
&gt;&gt;&gt;
&gt;&gt;&gt; u = User()
&gt;&gt;&gt; u.is_new
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5497">
                <li class="">

  <input type="radio" name="5497" id="5497-1501193547080" value="1501193547080" data-quiz-answer-id="1501193547080" data-quiz-question-id="5497" disabled="disabled" />
  <label for="5497-1501193547080"><p>is_new</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5497" id="5497-1501193551385" value="1501193551385" data-quiz-answer-id="1501193551385" data-quiz-question-id="5497" disabled="disabled" />
  <label for="5497-1501193551385"><p>Nothing</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5497" id="5497-1501193560101" value="1501193560101" data-quiz-answer-id="1501193560101" data-quiz-question-id="5497" disabled="disabled" />
  <label for="5497-1501193560101"><p>False</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5497" id="5497-1501193563180" value="1501193563180" data-quiz-answer-id="1501193563180" data-quiz-question-id="5497" disabled="disabled" checked="checked" />
  <label for="5497-1501193563180"><p>True</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5498" data-position="6">
            <div class=" clearfix" id="quiz_question-5498">

    <h4 class="quiz_question">

        Question #5
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; class User:
&gt;&gt;&gt;     id = 89
&gt;&gt;&gt;     name = &quot;no name&quot;
&gt;&gt;&gt;     __password = None
&gt;&gt;&gt;
&gt;&gt;&gt;     def __init__(self, new_name=None):
&gt;&gt;&gt;         self.is_new = True
&gt;&gt;&gt;         if new_name is not None:
&gt;&gt;&gt;             self.name = new_name
&gt;&gt;&gt;
&gt;&gt;&gt; u = User()
&gt;&gt;&gt; u.id
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5498">
                <li class="">

  <input type="radio" name="5498" id="5498-1501193588907" value="1501193588907" data-quiz-answer-id="1501193588907" data-quiz-question-id="5498" disabled="disabled" checked="checked" />
  <label for="5498-1501193588907"><p>89</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5498" id="5498-1501193595465" value="1501193595465" data-quiz-answer-id="1501193595465" data-quiz-question-id="5498" disabled="disabled" />
  <label for="5498-1501193595465"><p>id</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5498" id="5498-1501193598987" value="1501193598987" data-quiz-answer-id="1501193598987" data-quiz-question-id="5498" disabled="disabled" />
  <label for="5498-1501193598987"><p>User.id</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5498" id="5498-1501193609363" value="1501193609363" data-quiz-answer-id="1501193609363" data-quiz-question-id="5498" disabled="disabled" />
  <label for="5498-1501193609363"><p>Nothing</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5499" data-position="7">
            <div class=" clearfix" id="quiz_question-5499">

    <h4 class="quiz_question">

        Question #6
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; class User:
&gt;&gt;&gt;     id = 89
&gt;&gt;&gt;     name = &quot;no name&quot;
&gt;&gt;&gt;     __password = None
&gt;&gt;&gt;
&gt;&gt;&gt;     def __init__(self, new_name=None):
&gt;&gt;&gt;         self.is_new = True
&gt;&gt;&gt;         if new_name is not None:
&gt;&gt;&gt;             self.name = new_name
&gt;&gt;&gt;
&gt;&gt;&gt; u = User(&quot;John&quot;)
&gt;&gt;&gt; u.name
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5499">
                <li class="">

  <input type="radio" name="5499" id="5499-1501193617820" value="1501193617820" data-quiz-answer-id="1501193617820" data-quiz-question-id="5499" disabled="disabled" />
  <label for="5499-1501193617820"><p>name</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5499" id="5499-1501193620463" value="1501193620463" data-quiz-answer-id="1501193620463" data-quiz-question-id="5499" disabled="disabled" />
  <label for="5499-1501193620463"><p>None</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5499" id="5499-1501193624161" value="1501193624161" data-quiz-answer-id="1501193624161" data-quiz-question-id="5499" disabled="disabled" checked="checked" />
  <label for="5499-1501193624161"><p>John</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5499" id="5499-1501193671261" value="1501193671261" data-quiz-answer-id="1501193671261" data-quiz-question-id="5499" disabled="disabled" />
  <label for="5499-1501193671261"><p>no name</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5500" data-position="8">
            <div class=" clearfix" id="quiz_question-5500">

    <h4 class="quiz_question">

        Question #7
    </h4>

    <!-- Quiz question Body -->
    <p>What do these lines print?</p>

<pre><code>&gt;&gt;&gt; class User:
&gt;&gt;&gt;     id = 89
&gt;&gt;&gt;     name = &quot;no name&quot;
&gt;&gt;&gt;     __password = None
&gt;&gt;&gt;
&gt;&gt;&gt;     def __init__(self, new_name=None):
&gt;&gt;&gt;         self.is_new = True
&gt;&gt;&gt;         if new_name is not None:
&gt;&gt;&gt;             self.name = new_name
&gt;&gt;&gt;
&gt;&gt;&gt; u = User()
&gt;&gt;&gt; u.name
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5500">
                <li class="">

  <input type="radio" name="5500" id="5500-1501193677544" value="1501193677544" data-quiz-answer-id="1501193677544" data-quiz-question-id="5500" disabled="disabled" />
  <label for="5500-1501193677544"><p>name</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5500" id="5500-1501193746365" value="1501193746365" data-quiz-answer-id="1501193746365" data-quiz-question-id="5500" disabled="disabled" />
  <label for="5500-1501193746365"><p>None</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5500" id="5500-1501193755426" value="1501193755426" data-quiz-answer-id="1501193755426" data-quiz-question-id="5500" disabled="disabled" />
  <label for="5500-1501193755426"><p>John</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5500" id="5500-1501193762279" value="1501193762279" data-quiz-answer-id="1501193762279" data-quiz-question-id="5500" disabled="disabled" checked="checked" />
  <label for="5500-1501193762279"><p>no name</p>
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

    <div data-role="task19439" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-19439">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. My first square
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
    <p>Write an empty class <code>Square</code> that defines a square:</p>

<ul>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
Square = __import__(&#39;0-square&#39;).Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/$ ./0-main.py
&lt;class &#39;0-square.Square&#39;&gt;
{}
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
            <li>Directory: <code>python-classes</code></li>
            <li>File: <code>0-square.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19439" data-batch-id="843" data-toggle="modal" data-target="#task-19439-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19439-users-done-modal" data-task-id="19439" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "0. My first square"</h4>
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
              <span id="task-19439-score-info-score">0</span>/6
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19440" data-position="2" id="task-num-1">
      <div class="panel panel-default task-card " id="task-19440">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Square with size
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
    <p>Write a class <code>Square</code> that defines a square by: (based on <code>0-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code></li>
<li>Instantiation with <code>size</code> (no type/value verification)</li>
<li>You are not allowed to import any module</li>
</ul>

<p><strong>Why?</strong></p>

<p><em>Why <code>size</code> is private attribute?</em></p>

<p>The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute.
One way to have the control is to keep it privately.
You will see in next tasks how to get, update and validate the size value.</p>

<pre><code>guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
Square = __import__(&#39;1-square&#39;).Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./1-main.py
&lt;class &#39;1-square.Square&#39;&gt;
{&#39;_Square__size&#39;: 3}
&#39;Square&#39; object has no attribute &#39;size&#39;
&#39;Square&#39; object has no attribute &#39;__size&#39;
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
            <li>Directory: <code>python-classes</code></li>
            <li>File: <code>1-square.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19440" data-batch-id="843" data-toggle="modal" data-target="#task-19440-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19440-users-done-modal" data-task-id="19440" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "1. Square with size"</h4>
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
              <span id="task-19440-score-info-score">0</span>/13
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19441" data-position="3" id="task-num-2">
      <div class="panel panel-default task-card " id="task-19441">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Size validation
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
    <p>Write a class <code>Square</code> that defines a square by: (based on <code>1-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code></li>
<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code>

<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
Square = __import__(&#39;2-square&#39;).Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square(&quot;3&quot;)
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./2-main.py
&lt;class &#39;2-square.Square&#39;&gt;
{&#39;_Square__size&#39;: 3}
&lt;class &#39;2-square.Square&#39;&gt;
{&#39;_Square__size&#39;: 0}
&#39;Square&#39; object has no attribute &#39;size&#39;
&#39;Square&#39; object has no attribute &#39;__size&#39;
size must be an integer
size must be &gt;= 0
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
            <li>Directory: <code>python-classes</code></li>
            <li>File: <code>2-square.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19441" data-batch-id="843" data-toggle="modal" data-target="#task-19441-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19441-users-done-modal" data-task-id="19441" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "2. Size validation"</h4>
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
              <span id="task-19441-score-info-score">0</span>/11
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19442" data-position="4" id="task-num-3">
      <div class="panel panel-default task-card " id="task-19442">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Area of a square
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
    <p>Write a class <code>Square</code> that defines a square by: (based on <code>2-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code></li>
<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code>

<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
Square = __import__(&#39;3-square&#39;).Square

my_square_1 = Square(3)
print(&quot;Area: {}&quot;.format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print(&quot;Area: {}&quot;.format(my_square_2.area()))

guillaume@ubuntu:~/$ ./3-main.py
Area: 9
&#39;Square&#39; object has no attribute &#39;size&#39;
&#39;Square&#39; object has no attribute &#39;__size&#39;
Area: 25
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
            <li>Directory: <code>python-classes</code></li>
            <li>File: <code>3-square.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19442" data-batch-id="843" data-toggle="modal" data-target="#task-19442-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19442-users-done-modal" data-task-id="19442" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "3. Area of a square"</h4>
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
              <span id="task-19442-score-info-score">0</span>/8
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19443" data-position="5" id="task-num-4">
      <div class="panel panel-default task-card " id="task-19443">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Access and update private attribute
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
    <p>Write a class <code>Square</code> that defines a square by: (based on <code>3-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code>:

<ul>
<li>property <code>def size(self):</code> to retrieve it</li>
<li>property setter <code>def size(self, value):</code> to set it:

<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>You are not allowed to import any module</li>
</ul>

<p><strong>Why?</strong></p>

<p><em>Why a getter and setter?</em></p>

<p>Reminder: <code>size</code> is a private attribute. We did that to make sure we control the type and value.
Getter and setter methods are not 100% Python, but more OOP.
With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc.
Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.</p>

<pre><code>guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
Square = __import__(&#39;4-square&#39;).Square

my_square = Square(89)
print(&quot;Area: {} for size: {}&quot;.format(my_square.area(), my_square.size))

my_square.size = 3
print(&quot;Area: {} for size: {}&quot;.format(my_square.area(), my_square.size))

try:
    my_square.size = &quot;5 feet&quot;
    print(&quot;Area: {} for size: {}&quot;.format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
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
            <li>Directory: <code>python-classes</code></li>
            <li>File: <code>4-square.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19443" data-batch-id="843" data-toggle="modal" data-target="#task-19443-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19443-users-done-modal" data-task-id="19443" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "4. Access and update private attribute"</h4>
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
              <span id="task-19443-score-info-score">0</span>/17
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19448" data-position="6" id="task-num-5">
      <div class="panel panel-default task-card " id="task-19448">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Printing a square
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
    <p>Write a class <code>Square</code> that defines a square by: (based on <code>4-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code>:

<ul>
<li>property <code>def size(self):</code> to retrieve it</li>
<li>property setter <code>def size(self, value):</code> to set it:

<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>Public instance method: <code>def my_print(self):</code> that prints in stdout the square with the character <code>#</code>:

<ul>
<li>if <code>size</code> is equal to 0, print an empty line</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
Square = __import__(&#39;5-square&#39;).Square

my_square = Square(3)
my_square.my_print()

print(&quot;--&quot;)

my_square.size = 10
my_square.my_print()

print(&quot;--&quot;)

my_square.size = 0
my_square.my_print()

print(&quot;--&quot;)

guillaume@ubuntu:~/$ ./5-main.py
###
###
###
--
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
--

--
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
            <li>Directory: <code>python-classes</code></li>
            <li>File: <code>5-square.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19448" data-batch-id="843" data-toggle="modal" data-target="#task-19448-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19448-users-done-modal" data-task-id="19448" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "5. Printing a square"</h4>
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
              <span id="task-19448-score-info-score">0</span>/8
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19449" data-position="7" id="task-num-6">
      <div class="panel panel-default task-card " id="task-19449">
  <span id="user_id" data-id="9546"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. Coordinates of a square
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
    <p>Write a class <code>Square</code> that defines a square by: (based on <code>5-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code>:

<ul>
<li>property <code>def size(self):</code> to retrieve it</li>
<li>property setter <code>def size(self, value):</code> to set it:

<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>position</code>:

<ul>
<li>property <code>def position(self):</code> to retrieve it</li>
<li>property setter <code>def position(self, value):</code> to set it:

<ul>
<li><code>position</code> must be a tuple of 2 positive integers, otherwise raise a <code>TypeError</code> exception with the message <code>position must be a tuple of 2 positive integers</code><br></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>size</code> and optional <code>position</code>: <code>def __init__(self, size=0, position=(0, 0)):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>Public instance method: <code>def my_print(self):</code> that prints in stdout the square with the character <code>#</code>:

<ul>
<li>if <code>size</code> is equal to 0, print an empty line</li>
<li><code>position</code> should be use by using space - <strong>Don&rsquo;t fill lines by spaces</strong> when <code>position[1] &gt; 0</code></li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
Square = __import__(&#39;6-square&#39;).Square

my_square_1 = Square(3)
my_square_1.my_print()

print(&quot;--&quot;)

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print(&quot;--&quot;)

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print(&quot;--&quot;)

guillaume@ubuntu:~/$ ./6-main.py | tr &quot; &quot; &quot;_&quot; | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
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
            <li>Directory: <code>python-classes</code></li>
            <li>File: <code>6-square.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19449" data-batch-id="843" data-toggle="modal" data-target="#task-19449-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19449-users-done-modal" data-task-id="19449" data-batch-id="843">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "6. Coordinates of a square"</h4>
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
