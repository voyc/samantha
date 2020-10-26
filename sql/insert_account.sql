
/* taken from mai backup 2020 Oct 24 */

INSERT INTO account."user" (id, username, email, hashpassword, auth, access, tmregister, tmverify, hashtic, tmhashtic, newemail) VALUES (1, 'jhagstrand', 'john@hagstrand.com', '$2y$10$WXpUncg2BxU.ulLnIzNIDuhBM3qm9pElcpCu3gfD3L6bnFEl02E4C', 7, 1, '2019-10-14 03:05:09.43476-04', '2019-10-14 03:06:20.137-04', '$2y$10$dF3Uc6KGbWlxXkIZ.3XKHey6lPbU2xRXr9bcyQD/RXRC7xcWQJrgm', '2019-10-14 03:05:09.43476-04', NULL);
INSERT INTO account."user" (id, username, email, hashpassword, auth, access, tmregister, tmverify, hashtic, tmhashtic, newemail) VALUES (2, 'jvoyc', 'john@voyc.com', '$2y$10$g2pei8uG9EF9pnfMpNhF8uxVvB/B4c4I3IxEkHdkR7wBBlxLCbS/C', 7, 1, '2019-12-04 09:43:52.555272-05', '2019-12-04 09:45:11.641077-05', '$2y$10$/gwO3GlT7Pqh8lbfLOZ5m.qAVrs/Ol22At7JJx2BORYSZ96JWebSC', '2019-12-04 09:43:52.555272-05', NULL);
INSERT INTO account."user" (id, username, email, hashpassword, auth, access, tmregister, tmverify, hashtic, tmhashtic, newemail) VALUES (3, 'samantha', 'ptwjqoda@sharklasers.com', '$2y$10$w8nCb2MUCfhcY10eeqIrHur41auv9i/7FRjngT80UF4g8/kphCDF2', 7, 1, '2020-04-25 01:19:49.321104-04', '2020-04-25 01:21:56.556207-04', '$2y$10$tjnQo7.c6K/OFH6z2l00Fu4DTSLIqFxyzjFUpc7foac3oaHx2Mu/e', '2020-04-25 01:19:49.321104-04', NULL);

SELECT pg_catalog.setval('account.user_id_seq', 3, true);

INSERT INTO mai.alphabet (id, t, e, u, r, m, a) VALUES (1, 'ก', 'g', 'ก     ', ' ', 'm', ' ');
INSERT INTO mai.alphabet (id, t, e, u, r, m, a) VALUES (2, 'ข', 'k', 'ข     ', ' ', 'h', ' ');
