<template>
  <div class="container">
    <h2>Publish New Post</h2>
    <input v-model="title" class="form-control mb-2" placeholder="Title">
    <textarea v-model="body" class="form-control mb-2" rows="10" placeholder="Markdown Content"></textarea>
    <button class="btn btn-primary" @click="submitPost">Submit</button>
    <p v-if="success" class="text-success mt-2">✅ Article submitted!</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      title: '',
      body: '',
      success: false
    }
  },
  methods: {
    submitPost() {
      axios.post('http://localhost:5000/api/post', {
        title: this.title,
        body: this.body
      }).then(() => {
        this.success = true
        this.title = ''
        this.body = ''
      })
    }
  }
}
</script>
