<template>
  <div id="theBody">
    <h1>Bug Reports</h1>
    <p>Contact: e.lynn@usu.edu</p>
    <p><a href="https://github.com/emmalynnnn">GitHub</a></p>

    <div class="bug box">
      <br>
      <h2>Thank you for submitting a bug report!</h2>
      <p>I will get back to you promptly with an update if you included your contact information.</p>
      <br>

      <!-----------------------
      Title: HTML – How to Show Text Above Image on Hover
      Author: Singh, Yogesh
      12.5.2022 (accessed 1.25.2023)
      Available at: https://makitweb.com/html-how-to-show-text-above-image-on-hover/
      Modified by Emma Lynn
      -->

      <div class="content_img">
        <img src="../assets/bug.gif" alt="Animation of a bug." class="url-ex"/>
        <div>Yim, K. (2017). <em>This Walk Cycle Wednesday, it’s a pillbug!</em> https://ketrinadrawsalot.tumblr.com/post/145292711592/this-walk-cycle-wednesday-its-a-pillbug</div>
      </div>

      <!----------------------->
      <br>
    </div>
    <a href="/" class="btn btn-dark button">Back &lt;</a>
  </div>

</template>

<script>

export default {
  name: 'SubmittedComponent',
  data() {
    return {
    }
  },
}
</script>

<style>
#theBody {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: black;
  padding: 20px;
}

.box {
  border-radius: 10px;
  border-style: solid;
  border-width: 2px;
  width: 75%;
  text-align: center;
  margin: 0 auto;
}

.bug {
  background-color: #FFA559;
  border-color: #FFA559;
}

.bug a {
  color: black;
}

/* ---------------------
 Title: HTML – How to Show Text Above Image on Hover
 Author: Singh, Yogesh
 12.5.2022 (accessed 1.25.2023)
 Available at: https://makitweb.com/html-how-to-show-text-above-image-on-hover/
 Modified by Emma Lynn
*/

/* Parent Container */
.content_img{
  position: relative;
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 90%
}

/* Child Text Container */
.content_img div{
  position: absolute;
  bottom: 0;
  right: 0;
  background: black;
  color: white;
  margin-bottom: 5px;
  font-family: sans-serif;
  opacity: 0;
  visibility: hidden;
  -webkit-transition: visibility 0s, opacity 0.5s linear;
  transition: visibility 0s, opacity 0.5s linear;
  width: 100%
}

/* Hover on Parent Container */
.content_img:hover{
  cursor: pointer;
}

.content_img:hover div{
  width: 600px;
  padding: 8px 15px;
  visibility: visible;
  opacity: 0.7;
  margin-bottom: 15px;
  font-family: Verdana, serif;
}

/* --------------------- */

img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 100%;
}

</style>
