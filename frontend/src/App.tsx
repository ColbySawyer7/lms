import { createBrowserHistory as createHistory } from "history";
import simpleRestProvider from "ra-data-simple-rest";
import { Admin, fetchUtils, Resource, CustomRoutes } from "react-admin";
import { Route } from "react-router";
import MyLayout from "./components/AdminLayout";
import Dashboard from "./pages/Dashboard";
import { BookCreate, BookEdit, BookList } from "./pages/Books";
import { LibraryCreate, LibraryEdit, LibraryList } from "./pages/Library";
import { TransactionEdit, TransactionList } from "./pages/Transactions";

import LoginPage from "./pages/Login";
import { ProfileEdit } from "./pages/ProfileEdit";
import Register from "./pages/Register";
import { UserEdit, UserList } from "./pages/Users";
import authProvider from "./providers/authProvider";
import { basePath } from "./providers/env";
import PostIcon from "@mui/icons-material/PostAdd";
import PersonIcon from "@mui/icons-material/Person";
import MenuBookIcon from "@mui/icons-material/MenuBook";
import CollectionsIcon from "@mui/icons-material/Collections";
import ReceiptIcon from "@mui/icons-material/Receipt";

const httpClient = (url: string, options: any = {}) => {
  options.user = {
    authenticated: true,
    token: `Bearer ${localStorage.getItem("token")}`,
  };
  if (url.includes("/users/") && options.method === "PUT") {
    // We use PATCH for update on the backend for users, since PATCH is selective PUT, this change should be fine
    options.method = "PATCH";
  }
  return fetchUtils.fetchJson(url, options);
};

const dataProvider = simpleRestProvider(`${basePath}/api/v1`, httpClient);

const App = () => {
  return (
    <Admin
      disableTelemetry
      dataProvider={dataProvider}
      authProvider={authProvider}
      loginPage={LoginPage}
      history={createHistory()}
      layout={MyLayout}
      dashboard={Dashboard}
    >
      <CustomRoutes>
        <Route path="/my-profile" element={<ProfileEdit />} />
      </CustomRoutes>
      <CustomRoutes noLayout>
        <Route path="/register" element={<Register />} />
      </CustomRoutes>
      {(permissions) => [
        permissions.is_superuser === true ? (
          <Resource
            options={{ label: "Users" }}
            name="users"
            list={UserList}
            edit={UserEdit}
            icon={PersonIcon}
          />
        ) : null,
        permissions.is_superuser === true ? (
          <Resource
            options={{ label: "Transactions" }}
            name="transactions"
            list={TransactionList}
            edit={TransactionEdit}
            icon={ReceiptIcon}
          />
        ) : null,
        <Resource
          name="books"
          options={{ label: "Books" }}
          list={BookList}
          edit={BookEdit}
          create={BookCreate}
          icon={MenuBookIcon}
        />,
        <Resource
          name="libraries"
          options={{ label: "Libraries" }}
          list={LibraryList}
          edit={LibraryEdit}
          create={LibraryCreate}
          icon={CollectionsIcon}
        />,
      ]}
    </Admin>

  );
};

export default App;
