<template>
  <div class="container">
    <div class="content">
      <h1 class="page-title">Hello World 👋</h1>
      
      <div class="post-list">
        <div v-for="(posts, date) in groupedPosts" :key="date" class="date-group">
          <h2 class="date-title">{{ formatDate(date) }}</h2>
          <div v-for="post in posts" :key="post.id" class="post-card">
            <router-link :to="'/post/' + post.id">
              <h3 class="post-title">{{ post.title }}</h3>
              <p class="post-preview">{{ post.body.slice(0, 120) }}...</p>
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <!-- Simplified Date Picker -->
    <div class="sidebar">
      <flatpickr v-model="selectedDate" @change="filterPostsByDate" :config="config" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'
import Flatpickr from 'vue-flatpickr-component'
import 'flatpickr/dist/flatpickr.css'

export default {
  components: {
    Flatpickr
  },
  data() {
    return {
      posts: [],
      groupedPosts: {},
      selectedDate: null,
      config: {
        dateFormat: 'Y-m-d', // format for the selected date
        altInput: true, // enable a prettier input format
        altFormat: 'F j, Y', // the alternative format
        disableMobile: true, // disable the mobile date picker style
        theme: "light", // Use a light theme for the calendar
        inline: true, // Display the calendar inline
        showMonthArrow: false, // Disable the month navigation arrows
        maxDate: 'today', // Disable future dates
      }
    }
  },
  methods: {
    fetchPosts() {
      axios.get('https://ybenzou.work/api/posts')
        .then(res => {
          this.posts = res.data
          this.groupPostsByDate()
        })
    },
    groupPostsByDate() {
      const groups = this.posts.reduce((groups, post) => {
        const postDate = moment(post.date).format('YYYY-MM-DD')
        if (!groups[postDate]) {
          groups[postDate] = []
        }
        groups[postDate].push(post)
        return groups
      }, {})
      this.groupedPosts = groups
    },
    formatDate(date) {
      return moment(date).format('MMMM Do YYYY')
    },
    filterPostsByDate() {
      if (this.selectedDate) {
        const formattedDate = moment(this.selectedDate).format('YYYY-MM-DD')
        this.groupedPosts = { [formattedDate]: this.posts.filter(post => moment(post.date).isSame(formattedDate, 'day')) }
      } else {
        this.groupPostsByDate()
      }
    }
  },
  mounted() {
    this.fetchPosts()
  }
}
</script>

<style scoped>
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  background-color: #f9f9f9;
}

.container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: 0 auto;
  max-width: 1200px;
  padding: 40px;
}

.content {
  width: 75%;
}

.page-title {
  font-size: 48px;
  font-weight: 600;
  margin-bottom: 32px;
  color: #111;
  text-align: center;
}

.post-list {
  width: 100%;
}

.date-group {
  margin-bottom: 48px;
}

.date-title {
  font-size: 28px;
  font-weight: 600;
  margin-bottom: 16px;
  color: #444;
}

.post-card {
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.1);
  padding: 24px;
  margin-bottom: 24px;
  transition: all 0.3s ease;
}

.post-title {
  font-size: 22px;
  font-weight: 500;
  margin-bottom: 12px;
}

.post-preview {
  color: #555;
  font-size: 16px;
  line-height: 1.6;
}

.sidebar {
  width: 20%;
  padding: 20px;
  border-left: 1px solid #ddd;
}

.flatpickr {
  width: 100%;
  max-width: 300px;
  margin-top: 20px;
  border-radius: 8px;
  padding: 12px;
  background-color: #fff;
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.flatpickr input {
  font-size: 16px;
  padding: 8px;
  width: 100%;
  border-radius: 8px;
  border: 1px solid #ddd;
  background-color: #fafafa;
}

.flatpickr input:focus {
  border-color: #007aff;
  box-shadow: 0 0 10px rgba(0, 122, 255, 0.5);
}

.flatpickr .flatpickr-calendar {
  border-radius: 12px;
  padding: 16px;
}

.flatpickr .flatpickr-day:hover {
  background-color: #007aff;
  color: #fff;
}

.flatpickr .flatpickr-day.selected {
  background-color: #007aff;
  color: #fff;
}

</style>
