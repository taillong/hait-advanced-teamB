<template>
  <div>
    <button v-on:click="callApiv1">曲を知る</button>
    <p>あなたの声に合った曲は {{ songs }} です！</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Apiv1',
  data() {
    return {
      songs:'',
    }
  },
  methods: {
    callApiv1:() => {
      axios
      .get("http://127.0.0.1:8000/apiv1/")
      .then(response => (this.songs = response.data));
    }
  },
}
</script>

