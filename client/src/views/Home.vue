<template>
  <div class="home">
    <Ping msg="Hello world ping!!"/>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue';
import Ping from '@/components/Ping.vue';

export default {
  name: 'Home',
  components: {
    Ping,
  },
};
</script>
