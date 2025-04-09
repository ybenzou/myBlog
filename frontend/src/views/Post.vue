<template>
  <div class="container">
    <h1 class="post-title">{{ post.title }}</h1>
    <div class="post-content" v-html="renderedMarkdown"></div>
    <router-link to="/" class="back-link">← Back to Home</router-link>
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
    axios.get(`https://18.141.52.201/api/post/${this.$route.params.id}`)
      .then(res => {
        this.post = res.data
      })
  }
}
</script>

<style scoped>
.post-title {
  font-size: 48px;
  font-weight: 600;
  margin-bottom: 24px;
  color: #111;
  letter-spacing: -0.5px;
}

.post-content {
  font-size: 18px;
  line-height: 1.8;
  color: #444;
  margin-bottom: 40px;
}

.back-link {
  font-size: 16px;
  color: #007aff;
  text-decoration: none;
}

.back-link:hover {
  text-decoration: underline;
}
</style>
