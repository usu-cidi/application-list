<template>
  <h1>Emma's Applications</h1>
  <p>This is a simple static website that makes the web applications and documentation I've written
    for Utah State University available in one place.</p>
  <p>Contact: e.lynn@usu.edu</p>
  <p><a href="https://github.com/emmalynnnn/cidi-docs">Developer Documentation & Notes</a></p>
  <p><a href="https://github.com/emmalynnnn">GitHub</a></p>

  <div class="content">
    <h2>Applications and Tools</h2>

    <h3 style="text-align: center">CIDI</h3>

    <div class="box qa">
      <h4><a href="https://master.d3kepc58nvsh8n.amplifyapp.com/">QA Update</a></h4>
      <p><a href="https://github.com/emmalynnnn/cidi-monday-QA-automation/">Source</a></p>
    </div><br>

    <div class="box scripts">
      <h4>Canvas API Scripts</h4>
      <p><em>Instructor Stats</em>: Returns a report about the courses an instructor has taught</p>
      <p><em>Canvas User Info</em>: Returns the corresponding Canvas IDs, given a list of A-numbers</p>
      <p><em>Individual Quiz Data</em>: Generates a report showing student data from Canvas quiz attempts</p>
      <p><em>Summarized Quiz Data</em>: Generates a report showing a summary of student data from Canvas quiz attempts</p><br>
      <p>If you're interested in using one of these scripts, please contact e.lynn@usu.edu.</p>
    </div><br>

    <h3 style="text-align: center">Accessibility</h3>

    <div class="box ycct">
      <h4><a href="https://master.d18gulj4il0z61.amplifyapp.com/">YouTube Caption Tool (YCCT)</a></h4>
      <p><a href="https://github.com/emmalynnnn/access-caption-check">Source</a></p>
    </div><br>

    <h2>Documentation</h2>

    <div class="box doc1">
      <h4><a href="https://github.com/emmalynnnn/cidi-docs/blob/master/aws-deployment.md">Deploy a Web App With AWS</a></h4>
    </div><br>

    <div class="box doc2">
      <h4><a href="https://github.com/emmalynnnn/cidi-docs/blob/master/prep-board-for-qa.md">Set Up a New QA Term (Developer Instructions)</a></h4>
    </div><br>

    <div class="box doc3">
      <h4><a href="https://usu-accessibility.kbee.app/page/1am45cb-Oggvz02FCmsg_Vl_ZfeGBYwyfd4AJJNiRqFY/Deploying-Apps-to-AWS">Deploying Apps to AWS*</a></h4>
    </div><br>

    <div class="box doc4">
      <h4><a href="https://usu-accessibility.kbee.app/page/1zUgx3k0jwqLnLysNsPJo_zcNG90FhK_AdeGLQNcdLMg/Coding-Helps">Coding Helps and Best Practices*</a></h4>
    </div><br>

    <div class="box doc5">
      <h4><a href="https://usu-accessibility.kbee.app/page/1_miZU8qlbEhrY0StwBFP5ddrOCS-T9LHcDtfH0aeCsg/Development-Helps-for-External-Tools">Development Helps for External Tools*</a></h4>
    </div>

    <p>* contributed to</p>


    <h2>Bug Reports</h2>

    <div class="box bug">
      <h4><a href="https://master.d3kepc58nvsh8n.amplifyapp.com/bug-report">Bug Report Form</a></h4>
      <p><a href="https://github.com/emmalynnnn/cidi-monday-QA-automation/">Source</a></p>
    </div><br>
  </div>



</template>

<script>

export default {
  name: 'App',
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: black;
  /*margin-top: 20px;*/
}

.box {
  border-radius: 10px;
  border-style: solid;
  border-width: 2px;
  width: 75%;
  text-align: center;
  margin: 0 auto;
}

.qa {
  background-color: #BBD6E9;
  border-color: #BBD6E9;
}

.ycct {
  background-color: #569CAA;
  border-color: #569CAA;
}

.bug {
  background-color: #FFA559;
  border-color: #FFA559;
}

.doc1 {
  background-color: #D27685;
  border-color: #D27685;
}

.doc2 {
  background-color: #BE6DB7;
  border-color: #BE6DB7;
}

.doc3 {
  background-color: #9E4784;
  border-color: #9E4784;
}

.doc4 {
  background-color: #66347F;
  border-color: #66347F;
}

.doc4 a {
  color: #EEEEEE;
}

.doc5 {
  background-color: #37306B;
  border-color: #37306B;
}

.doc5 a {
  color: #EEEEEE;
}

.scripts {
  background-color: #A0C49D;
  border-color: #A0C49D;
}

a {
  color: black;
}

</style>
