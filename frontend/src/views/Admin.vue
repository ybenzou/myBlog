<template>
  <div class="container">
    <h2 class="page-title">Manage Posts 👋</h2>

    <!-- Publish New Post -->
    <div class="publish-section">
      <h3>Publish New Post</h3>
      <input v-model="title" class="input-field" placeholder="Enter title here" />
      <textarea v-model="body" class="textarea-field" placeholder="Write your post in Markdown" rows="10"></textarea>
      <button class="submit-btn" @click="submitPost">Submit</button>

      <p v-if="success" class="success-msg">✅ Post published successfully!</p>
    </div>

    <!-- List of Posts -->
    <div v-if="posts.length > 0" class="posts-list">
      <h3>Published Posts</h3>
      <div v-for="post in posts" :key="post.id" class="post-card">
        <h3>{{ post.title }}</h3>
        <button @click="deletePost(post.id)" class="delete-btn">Delete</button>
      </div>
    </div>
    <p v-else class="no-posts-msg">No posts available. Start by publishing a new one!</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      title: '',
      body: '',
      posts: [],
      success: false
    }
  },
  methods: {
    fetchPosts() {
      axios.get('https://52.221.182.99:5000/api/posts')
        .then(res => {
          this.posts = res.data
        })
    },
    submitPost() {
      axios.post('https://52.221.182.99:5000/api/post', {
        title: this.title,
        body: this.body
      })
      .then(() => {
        this.success = true
        this.title = ''
        this.body = ''
        this.fetchPosts()  // Refresh posts list after submission
      })
      .catch((err) => {
        console.error("Error while submitting post:", err)
      })
    },
    deletePost(postId) {
      if (confirm("Are you sure you want to delete this post?")) {
        axios.delete(`https://52.221.182.99:5000/api/post/${postId}`)
          .then(() => {
            this.success = false
            this.fetchPosts()  // Refresh posts list after deletion
          })
          .catch((err) => {
            console.error("Error deleting post:", err)
          })
      }
    }
  },
  mounted() {
    this.fetchPosts()  // Fetch posts when the page loads
  }
}
</script>

<style scoped>
.page-title {
  font-size: 42px;
  font-weight: 600;
  margin-bottom: 24px;
  color: #111;
  text-align: center;
}

.publish-section, .posts-list {
  margin-bottom: 40px;
}

.input-field, .textarea-field {
  width: 100%;
  padding: 16px;
  margin-bottom: 24px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 16px;
  background-color: #f9f9f9;
}

.submit-btn {
  background-color: #007aff;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 12px 24px;
  font-size: 18px;
  cursor: pointer;
  width: 100%;
  transition: background-color 0.3s ease;
}

.submit-btn:hover {
  background-color: #005bb5;
}

.delete-btn {
  background-color: #ff3b30;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  margin-top: 12px;
  transition: background-color 0.3s ease;
}

.delete-btn:hover {
  background-color: #d2301e;
}

.success-msg {
  color: #28a745;
  font-size: 16px;
  text-align: center;
  margin-top: 20px;
}

.no-posts-msg {
  color: #777;
  text-align: center;
}
</style>
