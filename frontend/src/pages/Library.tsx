import {
  Create,
  Datagrid,
  Edit,
  EditButton,
  List,
  SimpleForm,
  TextField,
  TextInput,
} from "react-admin";

export const LibraryList = (props: any) => (
  <List {...props} filters={[]}>
    <Datagrid>
      <TextField source="id" />
      <TextField source="name" />
      <TextField source="location" />
      <EditButton />
    </Datagrid>
  </List>
);

export const LibraryEdit = (props: any) => (
  <Edit {...props}>
    <SimpleForm>
      <TextInput source="name" />
      <TextInput source="location" />
    </SimpleForm>
  </Edit>
);

export const LibraryCreate = (props: any) => (
  <Create {...props}>
    <SimpleForm>
      <TextInput source="name" />
      <TextInput source="location" />
    </SimpleForm>
  </Create>
);
