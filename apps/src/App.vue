<template>
  <h1>Emma's Applications</h1>
  <p>This is a simple static website that makes the web applications and documentation I've written
    for Utah State University available in one place.</p>
  <p>Contact: e.lynn@usu.edu</p>
  <p><a href="https://github.com/emmalynnnn">GitHub</a></p>

  <h2>Applications</h2>

  <h3>CIDI</h3>

  <div class="box qa">
    <h4><a href="https://master.d3kepc58nvsh8n.amplifyapp.com/">QA Update</a></h4>
    <p><a href="https://github.com/emmalynnnn/cidi-monday-QA-automation/tree/main">Source</a></p>
  </div><br>

  <h3>Accessibility</h3>

  <div class="box ycct">
    <h4><a href="https://master.d18gulj4il0z61.amplifyapp.com/">YouTube Caption Tool</a></h4>
    <p><a href="https://github.com/emmalynnnn/access-caption-check">Source</a></p>
  </div><br>

  <h2>Documentation</h2>

  <h2>Bug Reports</h2>


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
  margin-top: 20px;
}

.box {
  border-radius: 10px;
  border-style: solid;
  border-width: 2px;
  cursor: pointer;
  letter-spacing: 1px;
  margin: 10px;
  padding: 3px 10px;
  width: 300px;
  text-align: center;
}

.qa {
  background-color: #BBD6E9;
  color: black;
  border-color: #BBD6E9;
}

.ycct {
  background-color: #569CAA;
  color: black;
  border-color: #569CAA;
}

a {
  color: black;
}

</style>
