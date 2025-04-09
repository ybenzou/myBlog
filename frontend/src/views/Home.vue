<template>
  <div class="container">
    <h1>👋 欢迎来到我的博客</h1>
    <div v-for="post in posts" :key="post.id" class="card mb-3">
      <div class="card-body">
        <h3><router-link :to="'/post/' + post.id">{{ post.title }}</router-link></h3>
        <p>{{ post.body.slice(0, 100) }}...</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      posts: []
    }
  },
  mounted() {
    axios.get('http://localhost:5000/api/posts')
      .then(res => {
        this.posts = res.data
      })
  }
}
</script>
