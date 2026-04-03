import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Infomaniak SDK for Python',
  description: 'Python SDK documentation for the Infomaniak API.',
  srcDir: 'src',
  base: '/infomaniak/',
  cleanUrls: true,
  themeConfig: {
    nav: [
      { text: 'Core', link: '/core/' },
    ],
    sidebar: [
      {
        text: 'Getting Started',
        items: [
          { text: 'Overview', link: '/' },
        ],
      },
      {
        text: 'Core',
        items: [
          { text: 'Core Overview', link: '/core/' },
          { text: 'Actions', link: '/core/actions' },
          { text: 'Countries', link: '/core/countries' },
          { text: 'Events', link: '/core/events' },
          { text: 'Languages', link: '/core/languages' },
          { text: 'Profile', link: '/core/profile' },
          { text: 'User', link: '/core/user' },
          { text: 'User Accounts', link: '/core/user/acccounts' },
          { text: 'User Teams', link: '/core/user/teams' },
        ],
      },
    ],
    search: {
      provider: 'local',
    },
  },
})
