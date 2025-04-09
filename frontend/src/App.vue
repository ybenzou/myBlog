<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style>
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  background-color: #f9f9f9;
  color: #111;
  font-size: 16px;
  line-height: 1.6;
}

.container {
  max-width: 1024px;
  margin: 0 auto;
  padding: 60px 24px;
}

a {
  text-decoration: none;
  color: #007aff;
}

a:hover {
  text-decoration: underline;
}
</style>
