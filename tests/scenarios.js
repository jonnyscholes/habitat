module.exports = [
  {
    label: "Login",
    path: "/login/?next=/admin/login",
    category: "Auth",
    unauthenticated: true,
    states: [
      {
        label: "Validation error",
        actions: [
          'click element [type="submit"]',
          "wait for element .error to be visible"
        ]
      }
    ]
  }
];
