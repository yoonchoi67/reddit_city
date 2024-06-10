const navList: NavItemType[] = [
    {
        _id: 1,
        name: 'Dashboard',
        icon: 'bi bi-boxes'
    },
    {
        _id: 2,
        name: 'F.A.Q',
        icon: 'bi bi-question-circle'
    },
    {
        _id: 3,
        name: 'Settings',
        icon: 'bi bi-gear'
    }

];

export interface NavItemType {
  _id: number;
  icon: string;
  name: string;
}

export default navList;