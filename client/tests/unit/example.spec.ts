import { shallowMount } from '@vue/test-utils';
import Timezone from '@/components/Timezone.vue';

describe('Timezone.vue', () => {
  it('renders props.msg when passed', () => {
    const msg = 'new message';
    const wrapper = shallowMount(Timezone, {
      propsData: { msg },
    });
    expect(wrapper.text()).toMatch(msg);
  });
});
