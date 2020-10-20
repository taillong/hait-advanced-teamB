<template>
  <div class="home">
    <Apiv1/>
  </div>
</template>

<script>
// @ is an alias to /src
import Apiv1 from '@/components/Apiv1.vue'

export default {
  name: 'Home',
  components: {
    Apiv1
  }
}
</script>
