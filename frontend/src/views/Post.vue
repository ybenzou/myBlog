<template>
  <div class="container">
    <h2>{{ post.title }}</h2>
    <div v-html="renderedMarkdown"></div>
    <router-link to="/">← Back to Home</router-link>
  </div>
</template>

<script>
import axios from 'axios'
import { marked } from 'marked'

export default {
  data() {
    return {
      post: {}
    }
  },
  computed: {
    renderedMarkdown() {
      return marked(this.post.body || '')
    }
  },
  mounted() {
    axios.get(`http://localhost:5000/api/post/${this.$route.params.id}`)
      .then(res => {
        this.post = res.data
      })
  }
}
</script>
