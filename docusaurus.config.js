// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)
const vercelHostname =
  process.env.VERCEL_PROJECT_PRODUCTION_URL || process.env.VERCEL_URL;
const siteUrl =
  process.env.SITE_URL ||
  (vercelHostname ? `https://${vercelHostname}` : 'https://matuteiglesias.github.io');
const baseUrl =
  process.env.BASE_URL || (vercelHostname ? '/' : '/atlas-pobreza-docs/');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Poverty Ecosystem Engineering',
  tagline: 'Arquitectura, contratos y estado del ecosistema argentino de medición de pobreza',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // GitHub Pages serves from /atlas-pobreza-docs/. Vercel deployments serve
  // from /. Explicit SITE_URL / BASE_URL environment variables override both.
  url: siteUrl,
  baseUrl,

  // GitHub Pages deployment config remains valid when that channel is used.
  organizationName: 'matuteiglesias',
  projectName: 'atlas-pobreza-docs',
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'es',
    locales: ['es'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          editUrl:
            'https://github.com/matuteiglesias/atlas-pobreza-docs/edit/main/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          editUrl:
            'https://github.com/matuteiglesias/atlas-pobreza-docs/edit/main/',
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'Poverty Ecosystem Engineering',
        logo: {
          alt: 'Poverty ecosystem engineering docs',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Documentación',
          },
          {to: '/blog', label: 'Blog', position: 'left'},
          {
            href: 'https://github.com/matuteiglesias/atlas-pobreza-docs',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Inicio',
                to: '/docs/',
              },
            ],
          },
          {
            title: 'Proyecto',
            items: [
              {
                label: 'Repositorio',
                href: 'https://github.com/matuteiglesias/atlas-pobreza-docs',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'Blog',
                to: '/blog',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/matuteiglesias/atlas-pobreza-docs',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Poverty Ecosystem Engineering. Construido con Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
